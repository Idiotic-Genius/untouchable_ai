import pygame

import constants as const


# Create the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(const.PLAYER_SIZE)
        self.image.fill(const.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = const.SCREEN_CENTER_POS
        self.speed = const.PLAYER_SPEED
        self.life = const.PLAYER_STARTING_LIFE
        self.score = 0

    def update(self):
        # Move the player left or right
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < const.SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < const.SCREEN_HEIGHT:
            self.rect.y += self.speed

    def increase_life(self, value: int) -> None:
        self.life += value

    def decrease_life(self, value: int) -> None:
        self.life -= value

    def increase_score(self, value: int) -> None:
        self.score += value