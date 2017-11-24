import pygame
from constants import *

radius = 10
color = gray
x = screen_width // 2
y = int(screen_height / 2.5)
mvmt = 4


def is_x_between_these_two_numbers(x, left, right):
    if x < right and x > left:
        return True
    else:
        return False


def has_ball_hit_paddle(paddle_top, paddle_left, paddle_right):
    ball_bottom = y + radius
    if ball_bottom < paddle_top:
        return False
    else:
        if is_x_between_these_two_numbers(x, paddle_left, paddle_right):
            return True


def handle_ball_collisions(paddle_top, paddle_left, paddle_right):
    if has_ball_hit_paddle(paddle_top, paddle_left, paddle_right):
        global mvmt
        mvmt = -mvmt


def draw_ball(screen):
    pygame.draw.circle(screen, laser_red, (x, y), radius)


def update_ball_position():
    global y
    y = y + mvmt
