import random


class ScreenService:
    @staticmethod
    def on_grid_random(scale=20, last_position=None):
        # x = random.randint(0, 550) // scale * 10
        # y = random.randint(0, 550) // scale * 10
        # print(x, y)
        new_position = (random.randrange(0, 550, scale), random.randrange(0, 550, scale))

        return ScreenService.on_grid_random(scale, last_position) if last_position == new_position else new_position
