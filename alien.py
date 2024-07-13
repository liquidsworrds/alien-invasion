import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (100, 70))
        self.rect = self.image.get_rect()

        # Generate new alien at the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien position
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
