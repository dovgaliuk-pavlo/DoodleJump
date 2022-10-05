import pygame

from classes.events import Events
from classes.screen import Screen
from classes.player import Player
from classes.world import World
from classes.sound import Sound

pygame.init()
pygame.display.set_caption("Doodle Jump")
timer = pygame.time.Clock()

default_width = 1080/2
default_height = 1920/2
default_speed = 5
default_gravity = .4
default_jump_height = 10
default_platforms_speed = 2.3

def main():
    jump = False
    x_change = 0
    y_change = 0
    points = 0

    screen = Screen(default_width, default_height)
    player = Player(177, 280, default_speed, default_gravity, default_jump_height, screen)
    world = World(screen)

    Sound.main_theme()
    running = True
    while running:
        timer.tick(screen.fps)
        screen.py_screen.blit(screen.bg_img, (0, 0))
        screen.py_screen.blit(player.py_player, (player.x, player.y))
        blocks = world.draw_platforms()

        world.move_platforms_down()
        world.create_new_platform()
        world.delete_old_platform()

        jump = player.check_collisions(blocks, jump, y_change)
        x_change, y_change = Events.check_player_vector(x_change, y_change, player)
        running = player.check_death()
        jump, y_change = player.update_player(jump, x_change, y_change)

        if points == 70: world.platforms_speed = default_platforms_speed
        points += 1
        if points % 300 == 0:
            if world.platforms_speed < default_platforms_speed*2: world.platforms_speed *= 1.03
            if world.disperse[0] > 450:  world.disperse = [int(dis*.99) for dis in world.disperse]
            if player.gravity < default_gravity*2: player.gravity *= 1.01
            if player.jump_height < default_jump_height*2: player.jump_height *= 1.01
            if player.speed < default_speed*1.5: player.speed += 0.1

        screen.draw_points(int(points/10))
        pygame.display.flip()

    Sound.death()

    while Events.check_continue_status():
        screen.py_screen.blit(screen.bg_img, (0, 0))
        screen.draw_defeat(int(points/10))
        pygame.display.flip()


while True:
    main()
