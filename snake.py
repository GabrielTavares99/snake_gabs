import pygame

from game_constants import SCALE


class Snake:
    _body = [(200, 200), (250, 200), (300, 200)]
    background_image = pygame.image.load('trak2_warn2c.tga')
    background = pygame.transform.scale(background_image, (SCALE, SCALE))

    def get_only_body(self):
        return self._body[1:]

    def get_body(self):
        return self._body

    def get_head(self):
        return self._body[0]

    def add(self):
        self._body.append((0, 0))

    def remove_from_index(self, index):
        self._body = self._body[0:index]

    def change_position(self, position):
        self._body[0] = position
