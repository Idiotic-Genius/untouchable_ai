import pygame
from enum import Enum

import constants as const


class Directions(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

# Create the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(const.PLAYER_SIZE)
        self.image.fill(const.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = const.SCREEN_CENTER_POS
        self.speed = const.PLAYER_SPEED
        self.time = const.PLAYER_STARTING_TIME
        self.score = 0

    def update(self):
        # Move the player left or right
        keys = pygame.key.get_pressed()
        if (
            keys[pygame.K_LEFT] or keys[pygame.K_a]
        ) and self.rect.left > 0:
            self.rect.x -= self.speed
        if (
            keys[pygame.K_RIGHT] or keys[pygame.K_d]
        ) and self.rect.right < const.SCREEN_WIDTH:
            self.rect.x += self.speed
        if (
            keys[pygame.K_UP] or keys[pygame.K_w]
        ) and self.rect.top > 0:
            self.rect.y -= self.speed
        if (
            keys[pygame.K_DOWN] or keys[pygame.K_s]
        ) and self.rect.bottom < const.SCREEN_HEIGHT:
            self.rect.y += self.speed

    def increase_time(self, value: int) -> None:
        self.time += value

    def decrease_time(self, value: int) -> None:
        self.time -= value

    def increase_score(self, value: int) -> None:
        self.score += value