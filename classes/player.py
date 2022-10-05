import pygame
from classes.sound import Sound


class Player:
    def __init__(self, x, y, speed, gravity, jump_height, screen):
        self.x = x
        self.y = y
        self.speed = speed
        self.gravity = gravity
        self.jump_height = jump_height
        self.double_jump = True
        self.screen = screen
        self.player_size_x = int(screen.height/14)
        self.player_size_y = int(screen.height / 14)
        self.left_player_image = pygame.transform.scale(pygame.image.load("images/doodle_left.png"),
                                                        (self.player_size_x, self.player_size_y))
        self.right_player_image = pygame.transform.scale(pygame.image.load("images/doodle_right.png"),
                                                         (self.player_size_x, self.player_size_y))
        self.py_player = self.right_player_image

    def check_death(self):
        return self.y < self.screen.height

    def scale_player(self):
        self.py_player = pygame.transform.scale(self.py_player,
                                                (self.player_size_x, self.player_size_y))

    def update_player(self, jump, x_change, y_change):
        if jump:
            y_change = self.jump()
            jump = False

        y_change += self.gravity

        self.y += y_change
        self.x += x_change

        self.scale_player()

        return jump, y_change

    def check_collisions(self, rect_list, jump, y_change):
        for rect in rect_list:
            if rect.colliderect([self.x + 10, self.y + self.player_size_x - self.player_size_x*0.2, 40, 10]) and not jump and y_change > 0:
                jump = True
                self.double_jump = True

        return jump

    def jump(self):
        Sound.jump()
        return -self.jump_height

    def left(self):
        self.py_player = self.left_player_image
        return -self.speed

    def right(self):
        self.py_player = self.right_player_image
        return self.speed



