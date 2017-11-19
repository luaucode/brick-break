import pygame
import pygame.constants
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

black = (0, 0, 0)
gray = (210, 210, 210)
white = (255, 255, 255)
cyan = (175, 231, 231)
laser_red = (255, 36, 36)


screen_width = 1364
screen_height = 742

left_down = False
right_down = False

paddle_width = 88
paddle_height = 7
paddle_left = (screen_width // 2) - (paddle_width // 2)
paddle_top = screen_height - 50
paddle_movement = 17

ball_radius = 10
plus_key = 270
minus_key = 269
ball_color = gray
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

def draw_paddle():
    pygame.draw.rect(screen, cyan, (paddle_left, paddle_top, paddle_width, paddle_height))


while not gameover:
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
    movement_left = min(paddle_movement, paddle_left - offset)
    paddle_right = paddle_left + paddle_width
    right_wall = screen_width - offset
    movement_right = min(paddle_movement, right_wall - paddle_right)
    if left_down:
        paddle_left = paddle_left - movement_left
    if right_down:
        paddle_left = paddle_left + movement_right


    # Drawing
    screen.fill(white)
    draw_brick_rows()
    pygame.draw.circle(screen, gray, (screen_width // 2, screen_height // 2), ball_radius)
    draw_paddle()

    pygame.display.update()
    clock.tick(60)
pygame.quit()
