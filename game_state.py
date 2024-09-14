from pygame import K_UP, K_RIGHT, K_LEFT, K_DOWN

from game_constants import DOWN, LEFT, RIGHT, UP, WINDOW_WIDTH, WINDOW_HEIGHT


class GameState:
    DIRECTION = None
    POINTS = 0

    @staticmethod
    def get_current_direction():
        return GameState.DIRECTION

    @staticmethod
    def change_direction(direction):
        GameState.DIRECTION = direction

    @staticmethod
    def direction_events(event):
        if event.key == K_UP and GameState.get_current_direction() != DOWN:
            GameState.change_direction(UP)
        elif event.key == K_RIGHT and GameState.get_current_direction() != LEFT:
            GameState.change_direction(RIGHT)
        elif event.key == K_LEFT and GameState.get_current_direction() != RIGHT:
            GameState.change_direction(LEFT)
        if event.key == K_DOWN and GameState.get_current_direction() != UP:
            GameState.change_direction(DOWN)

    @staticmethod
    def get_points():
        return GameState.POINTS

    @staticmethod
    def add_point(value):
        GameState.POINTS += value

    @staticmethod
    def subtract_point(value):
        points = GameState.POINTS - value
        GameState.POINTS = 0 if points < 0 else points

    @staticmethod
    def verify_border_out(snake):
        if snake.get_head()[0] < 0:
            snake.change_position((WINDOW_WIDTH, snake.get_head()[1]))
        elif snake.get_head()[0] > WINDOW_WIDTH:
            snake.change_position((0, snake.get_head()[1]))
        elif snake.get_head()[1] > WINDOW_HEIGHT:
            snake.change_position((snake.get_head()[0], 0))
        elif snake.get_head()[1] < 0:
            snake.change_position((snake.get_head()[0], WINDOW_HEIGHT))
