from os import path
import pygame


class Sound:
    music_location = "sound"

    @classmethod
    def load_music(cls, music_filename):
        pygame.mixer.music.load(path.join(cls.music_location, music_filename))

    @classmethod
    def load_sound(cls, sound_filename):
        return pygame.mixer.Sound(path.join(cls.music_location, sound_filename))

    @staticmethod
    def play(loops=0):
        pygame.mixer.music.play(loops)

    @staticmethod
    def set_volume(volume):
        pygame.mixer.music.set_volume(volume)

    @classmethod
    def main_theme(cls):
        main_theme_filename = "main_theme.mp3"
        cls.load_music(main_theme_filename)
        cls.set_volume(0.6)
        cls.play(-1)

    @classmethod
    def death(cls):
        death_filename = "death.mp3"
        cls.load_music(death_filename)
        cls.set_volume(1)
        cls.play()

    @classmethod
    def jump(cls):
        jump_filename = "jump.ogg"
        jump_sound_chanel = cls.load_sound(jump_filename)
        jump_sound_chanel.set_volume(0.2)
        jump_sound_chanel.play()