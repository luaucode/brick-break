import pygame

screen_width = 800
screen_height = 600
font_name = "plump"
font_size = 25

black = (0, 0, 0)
gray = (210, 210, 210)
white = (255, 255, 255)
cyan = (175, 231, 231)
laser_red = (255, 36, 36)
lime_green = (0, 245, 130)
chill_blue = (50, 145, 255)
mellow_yellow = (255, 255, 124)
voila_violet = (204, 153, 255)
rad_pink = (255, 76, 116)

background = pygame.image.load('images/background.jpg')
brick_width = 50
brick_height = 30

brick_count = screen_width // (brick_width + 1)
gap = screen_width - brick_count * (brick_width + 1)
offset = gap // 2
score_pos = (offset, screen_height - font_size - offset / 2)
lives_pos = (screen_width - offset * 7, screen_height - font_size - offset / 2)
debug_pos = (screen_width / 2, screen_height - font_size - offset / 2)

pdl_grwth = 20
pdl_shrnkth = 20
pdl_swfth = 2
pdl_slgth = 2
bll_flckrth = 95
bll_hdratn = 0.4
bll_hide_chance = 2
flckr_time = 7
