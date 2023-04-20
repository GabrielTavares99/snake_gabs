import pygame

from game_state import SCALE
from service.screen_service import ScreenService


class Apple:
    background_image = pygame.image.load('sprite_0.png')
    background = pygame.transform.scale(background_image, (SCALE, SCALE))
    position = ScreenService.on_grid_random(SCALE)
