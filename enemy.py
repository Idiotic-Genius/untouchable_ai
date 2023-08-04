import pygame
import random

import constants as const

# Create the Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((const.ENEMY_WIDTH, const.ENEMY_HEIGHT))
        self.image.fill(const.WHITE)
        self.rect = self.image.get_rect()
        self.spawn_left()

    def update(self):
        # Move the enemy down
        self.rect.x += self.speed

    def spawn(self):
        """Randomly spawn an enemy along the edge of the screen"""
        spawn_loc = random.choice(const.ENEMY_SPAWN_POS)

        if spawn_loc == const.SPAWN_TOP:
            self.rect.y = -self.rect.height
            self.rect.x = random.randrange(const.SCREEN_WIDTH - self.rect.width)
        elif spawn_loc == const.SPAWN_BOTTOM:
            self.rect.y = 0
            self.rect.x = 0
        elif spawn_loc == const.SPAWN_LEFT:
            self.rect.y = 0
            self.rect.x = 0
        elif spawn_loc == const.SPAWN_RIGHT:
            self.rect.y = 0
            self.rect.x = 0



