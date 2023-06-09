import sys
import random
import cairo
import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Odbijanie pileczki")

BALL_SIZE = 15
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = [2, 2]

PADDLE_WIDTH, PADDLE_HEIGHT = 15, 60
paddle_pos = [5, HEIGHT // 2 - PADDLE_HEIGHT // 2]
paddle_speed = 3

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle_pos[1] > 0:
        paddle_pos[1] -= paddle_speed
    if keys[pygame.K_DOWN] and paddle_pos[1] < HEIGHT - PADDLE_HEIGHT:
        paddle_pos[1] += paddle_speed

    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT - BALL_SIZE:
        ball_speed[1] = -ball_speed[1] * (1 + random.uniform(-0.1, 0.1))

    if (
        ball_pos[0] <= PADDLE_WIDTH
        and paddle_pos[1] <= ball_pos[1] <= paddle_pos[1] + PADDLE_HEIGHT
    ):
        ball_speed[0] = -ball_speed[0] * (1 + random.uniform(-0.1, 0.1))

    if ball_pos[0] >= WIDTH - BALL_SIZE:
        ball_speed[0] = -ball_speed[0] * (1 + random.uniform(-0.1, 0.1))

    data = bytearray(WIDTH * HEIGHT * 4)
    surface = cairo.ImageSurface.create_for_data(data, cairo.FORMAT_ARGB32, WIDTH, HEIGHT, WIDTH * 4)
    ctx = cairo.Context(surface)

    ctx.set_source_rgb(0, 0, 0)
    ctx.paint()

    ctx.set_source_rgb(1, 1, 1)
    ctx.rectangle(paddle_pos[0], paddle_pos[1], PADDLE_WIDTH, PADDLE_HEIGHT)
    ctx.fill()

    ctx.arc(ball_pos[0] + BALL_SIZE / 2, ball_pos[1] + BALL_SIZE / 2, BALL_SIZE / 2, 0, 2 * 3.14159265)
    ctx.fill()

    pygame_surface = pygame.image.frombuffer(data, (WIDTH, HEIGHT), 'RGBA')
    screen.blit(pygame_surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)