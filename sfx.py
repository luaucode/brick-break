import time

import pygame
import pygame.mixer

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

sfx_channel = pygame.mixer.Channel(0)
sfx_queue = []


effects = {
    'pshh': pygame.mixer.Sound('SFX/pshh.ogg'),
    'countdown1edit': pygame.mixer.Sound('SFX/countdown1edit.ogg'),
    'countdown2edit': pygame.mixer.Sound('SFX/countdown2edit.ogg'),
    'boing': pygame.mixer.Sound('SFX/boing.ogg'),
}

def play_sfx(sfx, times=1):
    effect = effects[sfx]
    for i in range(times):
        sfx_queue.append(effect)
    while sfx_queue:
        while sfx_channel.get_busy():
            time.sleep(0.1)
        effect = sfx_queue.pop(0)
        sfx_channel.play(effect)

def fast_sfx(sfx):
    effect = effects[sfx]
    effect.play()