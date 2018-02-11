import pygame
import ball
from constants import screen_width, screen_height, cyan, white

width = 88
height = 7
left = (screen_width // 2) - (width // 2)
top = screen_height - 50
bottom = top + height
mvmt_x = 8


def draw_paddle(screen):
    pygame.draw.rect(screen, white, (left, top, width, height))


def move_paddle(offset, left_down, right_down, ball_left, ball_top, ball_right, ball_bottom):
    global left
    global right
    movement_left = min(mvmt_x, left - offset)
    paddle_right = left + width
    right_wall = screen_width - offset
    movement_right = min(mvmt_x, right_wall - paddle_right)
    ok = check_ball_position(ball_left, ball_top, ball_right, ball_bottom, left_down, right_down)
    if left_down:
        if not ok:
            movement_left = left - ball_right
            ball.x -= movement_left
        left = left - movement_left
    if right_down:
        if not ok:
            movement_right = ball_left - right
            ball.x += movement_right
        left = left + movement_right
    return left


def check_ball_position(ball_left, ball_top, ball_right, ball_bottom, left_down, right_down):
    if ball_top > bottom or ball_bottom < top:
        return True
    right = left + width
    if ball_left > right and left_down:
        return True
    if ball_right < left and right_down:
        return True
    if right_down:
        return ball_left - right >= mvmt_x
    if left_down:
        return left - ball_right >= mvmt_x
    return True
