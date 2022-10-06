import pygame


class Screen:
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (128, 128, 128)
    yellow = (120, 210, 50)
    background = white

    def __init__(self, width, height, fps=60):
        self.width = width
        self.height = height
        self.fps = fps
        self.py_screen = pygame.display.set_mode([width, height])
        self.bg_img = pygame.image.load("images/background.jpg")
        self.bg_img = pygame.transform.scale(self.bg_img, (self.width, self.height))

    def draw_points(self, points):
        font_size = int(self.height*.05)
        def position_func(pos): pos.center = (self.width/2, font_size); return pos
        text = str(points)
        self.draw_text(font_size, position_func, text, Screen.black)

    def draw_defeat_message(self):
        font_size = 70
        def position_func(pos): pos.center = (self.width/2, self.height/2-font_size); return pos
        text = "Defeat"
        self.draw_text(font_size, position_func, text, Screen.black)

    def draw_after_death_score(self, points):
        font_size = 40
        def position_func(pos): pos.center = (self.width/2, self.height/2); return pos
        text = "Score:" + " " + str(points)
        self.draw_text(font_size, position_func, text, Screen.black)

    def draw_continue_message(self):
        font_size = 40
        def position_func(pos): pos.center = (self.width/2, self.height - font_size*3); return pos
        text = "Tap to continue"
        self.draw_text(font_size, position_func, text, Screen.black)

    def draw_text(self, font_size, position_func, text, color):
        font = pygame.font.Font("freesansbold.ttf", font_size)
        text = font.render(text, True, color)
        text_rect = position_func(text.get_rect())
        self.py_screen.blit(text, text_rect)
