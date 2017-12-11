from constants import *
from constants import brick_width

radius = 10
color = gray
x = screen_width // 2
y = int(screen_height / 2.5)
mvmt_y = 4
mvmt_x = 2


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


def handle_ball_paddle_collisions(paddle_top, paddle_left, paddle_right):
    if has_ball_hit_paddle(paddle_top, paddle_left, paddle_right):
        global mvmt_y
        mvmt_y = -mvmt_y


def handle_ball_brick_collisions(bricks):
    for b in bricks:
        bx = b[1]
        by = b[0]
        if x > bx and x < bx + brick_width and y > by and y < by + brick_height:
            bricks.remove(b)
            global mvmt_y
            mvmt_y = -mvmt_y


def draw_ball(screen):
    pygame.draw.circle(screen, laser_red, (x, y), radius)


def update_ball_y_position():
    global y
    y = y + mvmt_y


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
