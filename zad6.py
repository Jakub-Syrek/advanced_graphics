import pygame
import sys
import random


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

    
    screen.fill((0, 0, 0))

    
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(paddle_pos[0], paddle_pos[1], PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, (255, 255, 255), pygame.Rect(ball_pos[0], ball_pos[1], BALL_SIZE, BALL_SIZE))

    
    pygame.display.flip()
    clock.tick(60)
