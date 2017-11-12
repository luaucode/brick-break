import pygame
import pygame.constants

black = (0, 0, 0)
gray = (64, 64, 64)
white = (255, 255, 255)

display_width = 800
display_height = 600
ball_radius = 10
plus_key = 270
minus_key = 269
ball_color = gray

pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Brick Break')
clock = pygame.time.Clock()
gameover = False
while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYUP:
            if event.key == plus_key:
                ball_radius = ball_radius + 1
            if event.key == minus_key:
                ball_radius = ball_radius - 1

    # Drawing
    screen.fill(white)
    pygame.draw.rect(screen, gray, (0, 0, 50, 30))
    pygame.draw.circle(screen, gray, (display_width // 2, display_height // 2), ball_radius)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
