import pygame
from settings import Settings


class Jet():

    def __init__(self, screen):
        self.image = pygame.image.load("images/jet.png")

        self.screen = screen
        self.ai_set = Settings()
        self.image_rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.image_rect.centerx = float(self.screen_rect.centerx)
        self.image_rect.centery = float(self.screen_rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.rect = self.image_rect



    def blitme(self):
        self.screen.blit(self.image, self.image_rect)

    def update(self):
        if self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_set.jet_speed_factor
        elif self.moving_left and self.image_rect.left > 0:
            self.rect.centerx -= self.ai_set.jet_speed_factor
        elif self.moving_up and self.image_rect.top > self.screen_rect.top :
            self.rect.centery -= self.ai_set.jet_speed_factor
        elif self.moving_down and self.image_rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.ai_set.jet_speed_factor

        self.image_rect = self.rect

