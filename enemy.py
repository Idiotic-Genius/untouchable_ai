import pygame
import random

import constants as const

# Create the Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(const.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(const.SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed = random.randint(1, 4)

    def update(self):
        # Move the enemy down
        self.rect.y += self.speed
        # Respawn the enemy when it goes off the screen
        if self.rect.top > const.SCREEN_HEIGHT:
            self.rect.x = random.randrange(const.SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed = random.randint(1, 4)