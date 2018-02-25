import os
import random

import pygame.constants

import paddle
import state
from ball import (
    x as ball_x,
    y as ball_y,
    radius as ball_radius,
    update_ball_y_position,
    update_ball_x_position,
    handle_ball_wall_collisions,
    handle_ball_paddle_collisions,
    handle_ball_brick_collisions,
    draw_ball)
from constants import *
from paddle import *
from sfx import play_sfx
from text import render_text

os.environ['SDL_VIDEO_CENTERED'] = '1'

left_down = False
right_down = False

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Brick Break')
clock = pygame.time.Clock()
gameover = False
should_play_countdown = True


def play_countdown():
    play_sfx('countdown1edit', 3)
    play_sfx('countdown2edit')


row_count = 5

bricks = []


def populate_bricks():
    for row in range(row_count):
        for i in range(brick_count):
            nmbr = random.randint(1, 12)
            color = white
            effect = ''
            if nmbr == 8:
                color = lime_green
                effect = 'pdl_grw'
            elif nmbr == 9:
                color = chill_blue
                effect = 'pdl_shrnk'
            elif nmbr == 10:
                color = mellow_yellow
                effect = 'pdl_swft'
            elif nmbr == 11:
                color = voila_violet
                effect = 'pdl_slg'
            elif nmbr == 12:
                color = rad_pink
                effect = 'bll_flckr'
            brick = (row * (brick_height + 1), offset + i * (brick_width + 1), color, effect)
            bricks.append(brick)


def draw_bricks():
    for b in bricks:
        x = b[1]
        y = b[0]
        pygame.draw.rect(screen, b[2], (x, y, brick_width, brick_height))


populate_bricks()

# main loop
while state.lives > 0:
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
    update_ball_y_position()
    update_ball_x_position()
    handle_ball_wall_collisions()
    handle_ball_paddle_collisions(paddle.top, paddle.left, paddle.left + paddle.width, left_down, right_down)
    handle_ball_brick_collisions(bricks)
    paddle_left = move_paddle(offset, left_down, right_down,
                              ball_x - ball_radius, ball_y - ball_radius,
                              ball_x + ball_radius, ball_y + ball_radius)


    # Drawing
    screen.blit(background, (0, 0))
    draw_bricks()
    draw_paddle(screen)
    draw_ball(screen)
    render_text(screen, f'Score: {state.score}', score_pos)
    render_text(screen, f'Lives: {state.lives}', lives_pos)

    pygame.display.update()
    clock.tick(90)

    if should_play_countdown:
        pygame.mixer.music.load("SFX/backgroundmusic.ogg")
        pygame.mixer.music.play(-1)
        play_countdown()
        should_play_countdown = False
pygame.quit()
