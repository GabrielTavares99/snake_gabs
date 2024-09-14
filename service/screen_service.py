import random

from game_constants import WINDOW_WIDTH, WINDOW_HEIGHT


class ScreenService:

    @staticmethod
    def put_in_screem(screen, item, positions):
        for position in positions:
            screen.blit(item, position)

    @staticmethod
    def on_grid_random(scale=50, last_position=None):
        x = random.randrange(0, WINDOW_WIDTH - scale, scale)
        y = random.randrange(0, WINDOW_HEIGHT - scale, scale)
        new_position = (x, y)

        # return ScreenService.on_grid_random(scale, last_position) if last_position == new_position else new_position
        return new_position
