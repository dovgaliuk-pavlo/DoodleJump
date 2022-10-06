import pygame


class Events:
    @classmethod
    def check_player_vector(cls, x_change, y_change, player):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change += player.left()
                if event.key == pygame.K_d:
                    x_change += player.right()
                if event.key == pygame.K_s:
                    y_change += 10
                if (event.key == pygame.K_w or event.key == pygame.K_SPACE) and player.double_jump:
                    y_change = player.jump() + 2
                    player.double_jump = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    x_change = 0
                if event.key == pygame.K_d:
                    x_change = 0
        return x_change, y_change

    @classmethod
    def check_continue_status(cls):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                else:
                    return False
        return True
