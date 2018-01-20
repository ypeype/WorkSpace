import sys
import pygame
from settings import Settings
from jet import Jet
import game_functions as gf


def run_game():
    pygame.init()
    ai_set = Settings()

    screen = pygame.display.set_mode((ai_set.screen_width, ai_set.screen_height))
    pygame.display.set_caption(ai_set.screen_title)
    jet = Jet(screen)

    while True:
        gf.check_events(jet)
        gf.screen_update(screen,jet,ai_set)



run_game()