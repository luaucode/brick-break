import pygame

from constants import screen_width, screen_height, cyan, white

width = 88
height = 7
left = (screen_width // 2) - (width // 2)
top = screen_height - 50
mvmt_y = 8


def draw_paddle(screen):
    pygame.draw.rect(screen, white, (left, top, width, height))


def move_paddle(offset, left_down, right_down):
    global left
    movement_left = min(mvmt_y, left - offset)
    paddle_right = left + width
    right_wall = screen_width - offset
    movement_right = min(mvmt_y, right_wall - paddle_right)
    if left_down:
        left = left - movement_left
    if right_down:
        left = left + movement_right
    return left