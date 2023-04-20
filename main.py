import random

import pygame
from pygame import QUIT, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT

from apple import Apple
from game_state import FPS, WINDOW_WIDTH, WINDOW_HEIGHT, SCALE
from service.audio_service import AudioService
from service.physics_service import PhysicsService
from service.screen_service import ScreenService

pygame.init()
AudioService.init()

pygame.display.set_caption('Snake Gabs')

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

snake = [(200, 200), (250, 200), (2300, 200)]

snake_skin = pygame.transform.scale(pygame.image.load('trak2_warn2c.tga'), (SCALE, SCALE))

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

direction = None

# apple = pygame.Surface((10, 10))

apple = Apple()

# apple.fill((255, 0, 0))

b_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
screen.fill(b_color)

screen.blit(apple.background, ScreenService.on_grid_random(SCALE))

# pygame.mixer.music.load("background-music.mp3")
# pygame.mixer.music.play(-1)

game_font = pygame.font.SysFont("Arial", 24)

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

for pos in snake:
    screen.blit(snake_skin, pos)
    pygame.display.update()

clock = pygame.time.Clock()

start = False
points = 0

target_time = pygame.time.get_ticks() + 3000  # 3 seconds from now

apple = Apple()

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP and direction != DOWN:
                direction = UP
            elif event.key == K_RIGHT and direction != LEFT:
                direction = RIGHT
            elif event.key == K_LEFT and direction != RIGHT:
                direction = LEFT
            if event.key == K_DOWN and direction != UP:
                direction = DOWN

    if PhysicsService.has_collision(snake[0], apple.position):
        apple.position = ScreenService.on_grid_random(SCALE)
        points += 1
        snake.append((0, 0))
        AudioService.play('eat')
        text_surface = game_font.render('POINTS: {}'.format(points), True, (255, 255, 255))
        text_box.fill((255, 0, 0))

    for index, i in enumerate(snake[1:]):
        if PhysicsService.has_collision(snake[0], i):
            AudioService.play('lose')
            points -= len(snake[index:])
            points = 0 if points < 0 else points
            snake = snake[0:index]
            text_surface = game_font.render('POINTS: {}'.format(points), True, (255, 255, 255))
            text_box.fill((255, 0, 0))

    if start:
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i - 1][0], snake[i - 1][1])

    if direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - SCALE)
        start = True

    if direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + SCALE)
        start = True

    if direction == LEFT:
        snake[0] = (snake[0][0] - SCALE, snake[0][1])
        start = True

    if direction == RIGHT:
        snake[0] = (snake[0][0] + SCALE, snake[0][1])
        start = True

    if pygame.time.get_ticks() >= target_time:
        target_time = pygame.time.get_ticks() + 3000  # 3 seconds from now
        b_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    screen.fill(b_color)

    for pos in snake:
        screen.blit(snake_skin, pos)
    screen.blit(apple.background, apple.position)

    screen.blit(text_box, text_box_rect)
    text_box.blit(text_surface, text_rect)

    pygame.display.update()
