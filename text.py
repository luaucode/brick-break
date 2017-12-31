from constants import *


def render_text(screen, text, pos):
    font = pygame.font.SysFont(font_name, font_size)
    text = font.render(text, True, white)
    screen.blit(text, pos)
