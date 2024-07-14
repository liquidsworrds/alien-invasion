import pygame.font


class Button():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('images/start_btn.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 60))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def draw_button(self):
        self.screen.blit(self.image, self.rect)
