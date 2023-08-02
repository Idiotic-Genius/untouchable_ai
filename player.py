import pygame

import constants as const


# Create the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(const.RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = const.SCREEN_WIDTH // 2
        self.rect.bottom = const.SCREEN_HEIGHT - 10
        self.speed = 5

    def update(self):
        # Move the player left or right
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        # Ensure the player stays within the screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > const.SCREEN_WIDTH:
            self.rect.right = const.SCREEN_WIDTH