import pygame
import sys


def check_events(jet):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                jet.moving_right = True
            elif event.key == pygame.K_LEFT:
                jet.moving_left = True
            elif event.key == pygame.K_UP:
                jet.moving_up = True
            elif event.key == pygame.K_DOWN:
                jet.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                jet.moving_right = False
            elif event.key == pygame.K_LEFT:
                jet.moving_left = False
            elif event.key == pygame.K_UP:
                jet.moving_up = False
            elif event.key == pygame.K_DOWN:
                jet.moving_down = False


def screen_update(screen,jet,ai_set):
    screen.fill(ai_set.screen_bg_color)
    jet.blitme()
    jet.update()
    pygame.display.flip()





