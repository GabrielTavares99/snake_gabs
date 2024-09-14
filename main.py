import random

import pygame
from pygame import QUIT, KEYDOWN

from apple import Apple
from game_constants import FPS, WINDOW_WIDTH, WINDOW_HEIGHT, SCALE, DOWN, UP, RIGHT, LEFT
from game_state import GameState
from rock import Rock
from service.audio_service import AudioService
from service.physics_service import PhysicsService
from service.screen_service import ScreenService
from snake import Snake

pygame.init()
AudioService.init()

pygame.display.set_caption('Snake Gabs')
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
game_font = pygame.font.SysFont("Arial", 24)

apple = Apple()
snake = Snake()

b_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
screen.fill(b_color)

screen.blit(apple.background, ScreenService.on_grid_random(SCALE))

# pygame.mixer.music.load("background-music.mp3")
# pygame.mixer.music.play(-1)


text_box_width = 200
text_box_height = 50

text_box = pygame.Surface((text_box_width, text_box_height))
text_box.fill((255, 0, 0))
text_box_rect = (10, 10)
# text_box_rect.center = (window_width // 2, window_height // 2)

text_surface = game_font.render("POINTS: 0", True, (255, 255, 255))
text_rect = (10, 10)
# text_rect.center = (text_box_width // 2, text_box_height // 2)  # center the text on the text box surface
text_box.blit(text_surface, text_rect)

ScreenService.put_in_screem(screen, snake.background, snake.get_body())

pygame.display.update()
clock = pygame.time.Clock()

start = False

target_time = pygame.time.get_ticks() + 3000  # 3 seconds from now

generate_rock = pygame.time.get_ticks() + 10 * 1000  # 3 seconds from now
rocks = []
while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

        if event.type == KEYDOWN:
            GameState.direction_events(event)

    if not pygame.display.get_init():
        break

    GameState.verify_border_out(snake)

    if PhysicsService.has_collision(snake.get_head(), apple.position):
        apple.position = ScreenService.on_grid_random(SCALE)
        GameState.add_point(1)
        snake.add()
        AudioService.play('eat')
        text_surface = game_font.render('POINTS: {}'.format(GameState.get_points()), True, (255, 255, 255))
        text_box.fill((255, 0, 0))

    for index, i in enumerate(snake.get_only_body()):
        if PhysicsService.has_collision(snake.get_head(), i):
            AudioService.play('lose')
            GameState.subtract_point(len(snake.get_body()[index:]))
            snake.remove_from_index(index)
            text_surface = game_font.render('POINTS: {}'.format(GameState.get_points()), True, (255, 255, 255))
            text_box.fill((255, 0, 0))

    if start:
        for i in range(len(snake.get_body()) - 1, 0, -1):
            snake.get_body()[i] = (snake.get_body()[i - 1][0], snake.get_body()[i - 1][1])

    if GameState.get_current_direction() == UP:
        snake.get_body()[0] = (snake.get_body()[0][0], snake.get_body()[0][1] - SCALE)
        start = True

    if GameState.get_current_direction() == DOWN:
        snake.get_body()[0] = (snake.get_body()[0][0], snake.get_body()[0][1] + SCALE)
        start = True

    if GameState.get_current_direction() == LEFT:
        snake.get_body()[0] = (snake.get_body()[0][0] - SCALE, snake.get_body()[0][1])
        start = True

    if GameState.get_current_direction() == RIGHT:
        snake.get_body()[0] = (snake.get_body()[0][0] + SCALE, snake.get_body()[0][1])
        start = True

    if pygame.time.get_ticks() >= target_time:
        target_time = pygame.time.get_ticks() + 3000  # 3 seconds from now
        b_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    screen.fill(b_color)

    if pygame.time.get_ticks() >= generate_rock:
        generate_rock = pygame.time.get_ticks() + 10 * 1000
        # print('gener', rock.position)
        rocks.append(Rock())

    for pos in snake.get_body():
        screen.blit(snake.background, pos)

    for rock in rocks:
        print(rock.position)
        screen.blit(rock.background, rock.position)

    screen.blit(apple.background, apple.position)

    screen.blit(text_box, text_box_rect)
    text_box.blit(text_surface, text_rect)

    pygame.display.update()
