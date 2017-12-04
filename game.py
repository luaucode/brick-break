import os

import pygame.constants

import paddle
from ball import update_ball_position, handle_ball_paddle_collisions, draw_ball, handle_ball_brick_collisions
from constants import *
from constants import brick_width, brick_height
from paddle import draw_paddle, move_paddle

os.environ['SDL_VIDEO_CENTERED'] = '1'

left_down = False
right_down = False

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Brick Break')
clock = pygame.time.Clock()
gameover = False

row_count = 5

brick_count = screen_width // (brick_width + 1)
gap = screen_width - brick_count * (brick_width + 1)
offset = gap // 2

bricks = []

def populate_bricks():
    for row in range(row_count):
        for i in range(brick_count):
            pair = (row * (brick_height + 1), offset + i * (brick_width + 1))
            bricks.append(pair)


def draw_bricks():
    for b in bricks:
        x = b[1]
        y = b[0]
        pygame.draw.rect(screen, gray, (x, y, brick_width, brick_height))

populate_bricks()
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
    handle_ball_paddle_collisions(paddle.top, paddle.left, paddle.left + paddle.width)
    handle_ball_brick_collisions(bricks)

    # Drawing
    screen.blit(background,(0,0))
    draw_bricks()
    draw_paddle(screen)
    draw_ball(screen)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
