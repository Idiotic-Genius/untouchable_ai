import pygame
import random

import constants as const

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(const.ENEMY_SIZE)
        self.image.fill(const.RED)
        self.rect = self.image.get_rect()
        self.spawn()

    def update(self):
        if self.spawn_loc == const.ENEMY_SPAWN_TOP:
            if self.rect.y > const.SCREEN_HEIGHT + self.rect.height:
                self.spawn()
            self.rect.y += self.speed
        elif self.spawn_loc == const.ENEMY_SPAWN_BOTTOM:
            if self.rect.y < -self.rect.height:
                self.spawn()
            self.rect.y -= self.speed
        elif self.spawn_loc == const.ENEMY_SPAWN_LEFT:
            if self.rect.x > const.SCREEN_WIDTH + self.rect.width:
                self.spawn()
            self.rect.x += self.speed
        elif self.spawn_loc == const.ENEMY_SPAWN_RIGHT:
            if self.rect.x < -self.rect.width:
                self.spawn()
            self.rect.x -= self.speed

    def spawn(self):
        self.spawn_loc = random.choice(const.ENEMY_SPAWN_POS)
        self.speed = round(
            random.uniform(const.ENEMY_SPEED_MIN, const.ENEMY_SPEED_MAX),
            2
        )

        if self.spawn_loc == const.ENEMY_SPAWN_TOP:
            self.rect.y = random.randrange(
                -self.rect.height*5,
                -self.rect.height
            )
            self.rect.x = random.randrange(
                const.SCREEN_WIDTH - self.rect.width
            )

        elif self.spawn_loc == const.ENEMY_SPAWN_BOTTOM:
            self.rect.y = random.randrange(
                const.SCREEN_HEIGHT + self.rect.height,
                const.SCREEN_HEIGHT + self.rect.height*5,
            )
            self.rect.x = random.randrange(
                const.SCREEN_WIDTH - self.rect.width
            )

        elif self.spawn_loc == const.ENEMY_SPAWN_LEFT:
            self.rect.y = random.randrange(
                const.SCREEN_HEIGHT - self.rect.height
            )
            self.rect.x = random.randrange(
                -self.rect.width*5,
                -self.rect.width
            )

        elif self.spawn_loc == const.ENEMY_SPAWN_RIGHT:
            self.rect.y = random.randrange(
                const.SCREEN_HEIGHT - self.rect.height
            )
            self.rect.x = random.randrange(
                const.SCREEN_WIDTH + self.rect.width,
                const.SCREEN_WIDTH + self.rect.width*5
            )

