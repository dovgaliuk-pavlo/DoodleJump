import random

import pygame


class World:
    def __init__(self, screen):
        rand = lambda: random.randint(0, screen.width - 50)
        self.platforms = [[rand(), screen.height - 100*i, 80, 10] for i in range(int(screen.height/100))]
        self.platforms_speed = 0
        self.screen = screen
        self.disperse = [int(self.screen.height) - 400, int(self.screen.height) - 100]

    def draw_platforms(self):
        blocks = []
        for platform in self.platforms:
            block = pygame.draw.rect(self.screen.py_screen, self.screen.black, platform, 0, 4)
            blocks.append(block)
        return blocks

    def move_platforms_down(self):
        for platform in self.platforms:
            platform[1] += self.platforms_speed

    def create_new_platform(self):
        create_platform = True
        for platform in self.platforms:
            disperse = random.randint(self.disperse[0], self.disperse[1])
            if platform[1] < self.screen.height - disperse:
                create_platform = False

        if create_platform:
            x = random.randint(0, self.screen.width - 50)
            self.platforms.append([x, 0, 80, 10])

    def delete_old_platform(self):
        for platform in self.platforms:
            if platform[1] > self.screen.height:
                del platform