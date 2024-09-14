import pygame

from game_constants import SCALE
from service.screen_service import ScreenService


class Rock:
    background_image = pygame.image.load('images/rock.png')
    background = pygame.transform.scale(background_image, (SCALE, SCALE))
    position = None

    def __init__(self):
        self.position = ScreenService.on_grid_random(SCALE)
