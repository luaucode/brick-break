from random import randint
import paddle
from constants import *
from constants import brick_width
import state
from sfx import fast_sfx


def reset_ball():
    global x
    global y
    x = screen_width // 2
    y = int(screen_height / 2.5)
    global mvmt_y
    global mvmt_x
    mvmt_x = randint(-2, 2)
    mvmt_y = 4


radius = 10
color = gray
x = 0
y = 0
mvmt_y = 0
mvmt_x = 0
reset_ball()


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


def handle_ball_paddle_collisions(paddle_top, paddle_left, paddle_right, left_down, right_down):
    if has_ball_hit_paddle(paddle_top, paddle_left, paddle_right):
        fast_sfx("boing")
        global mvmt_x
        global mvmt_y
        mvmt_y = -mvmt_y
        if left_down:
            mvmt_x -= 1
        if right_down:
            mvmt_x += 1


def handle_ball_brick_collisions(bricks):
    for b in bricks:
        bx = b[1]
        by = b[0]
        if x > bx and x < bx + brick_width and y > by and y < by + brick_height:
            fast_sfx("pshh")
            bricks.remove(b)
            global mvmt_y
            mvmt_y = -mvmt_y
            state.score = state.score + 50


def calculate_dy(paddle_right, paddle_left, paddle_top):
    b_p_distance = paddle_top - y + radius
    if b_p_distance > mvmt_y:
        return mvmt_y

    if x > paddle_right or x < paddle_left:
        return mvmt_y

    if mvmt_y < 0:
        return mvmt_y

    return b_p_distance


def draw_ball(screen):
    pygame.draw.circle(screen, white, (x, y), radius)


def update_ball_y_position():
    global y
    paddle_right = paddle.left + paddle.width
    dy = calculate_dy(paddle_right, paddle.left, paddle.top)
    y = y + dy
    if y > screen_height:
        state.lives = state.lives - 1
        reset_ball()


def update_ball_x_position():
    global x
    x = x + mvmt_x


def handle_ball_wall_collisions():
    right_wall = screen_width - offset
    if x >= right_wall:
        global mvmt_x
        mvmt_x = -mvmt_x
    left_wall = offset
    if x <= left_wall:
        mvmt_x = -mvmt_x
    ceiling = 0
    if y <= ceiling:
        global mvmt_y
        mvmt_y = -mvmt_y
