import pygame
from constants import *

radius = 10
color = gray
x = screen_width // 2
y = int(screen_height / 2.5)
mvmt = 1


def has_ball_hit_paddle(paddle_top):
    ball_bottom = y + radius
    if ball_bottom < paddle_top:
        return False
    else:
        return True


def handle_ball_collisions(paddle_top):
    if has_ball_hit_paddle(paddle_top):
        global mvmt
        mvmt = -mvmt


def draw_ball(screen):
    pygame.draw.circle(screen, laser_red, (x, y), radius)


def update_ball_position():
    global y
    y = y + mvmt
