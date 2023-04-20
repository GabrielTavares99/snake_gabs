import pygame


class AudioService:
    AUDIOS = None

    @staticmethod
    def init():
        AudioService.AUDIOS = {
            'eat': pygame.mixer.Sound("eat.wav"),
            'lose': pygame.mixer.Sound("lose-music.wav")
        }

    @staticmethod
    def play(description):
        return AudioService.AUDIOS[description].play()
