import os

import pygame
import pygame.constants

from ball import update_ball_position, handle_ball_collisions, draw_ball
from constants import *
import paddle
from paddle import draw_paddle, move_paddle

os.environ['SDL_VIDEO_CENTERED'] = '1'

left_down = False
right_down = False

brick_width = 50
brick_height = 30

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Brick Break')
clock = pygame.time.Clock()
gameover = False

row_count = 5

brick_count = screen_width // (brick_width + 1)
gap = screen_width - brick_count * (brick_width + 1)
offset = gap // 2




def draw_brick_row(height):
    for i in range(brick_count):
        pygame.draw.rect(screen, gray, (offset + (brick_width + 1) * i, height, brick_width, brick_height))


def draw_brick_rows():
    for i in range(row_count):
        draw_brick_row((brick_height + 1) * i)


# main loop
while not gameover:
    # Handle key presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_down = True
            if event.key == pygame.K_RIGHT:
                right_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_down = False
            if event.key == pygame.K_RIGHT:
                right_down = False

    # Move paddle if needed
    paddle_left = move_paddle(offset, left_down, right_down)
    update_ball_position()
    handle_ball_collisions(paddle.top, paddle.left, paddle.left + paddle.width)

    # Drawing
    screen.blit(background,(0,0))
    draw_brick_rows()
    draw_paddle(screen)
    draw_ball(screen)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
