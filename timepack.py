import random
import pygame

import constants as const


class TimePack(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface(const.TIMEPACK_SIZE)
        self.image.fill(const.GREEN)
        self.rect = self.image.get_rect()
        self.value = const.TIMEPACK_VALUE
        self.spawn()

    def spawn(self) -> None:
        self.rect.centerx = random.randrange(
            const.SCREEN_WIDTH - self.rect.width
        )
        self.rect.centery = random.randrange(
            const.SCREEN_HEIGHT - self.rect.height
        )

    def get_pos(self) -> tuple[int, int]:
        return self.rect.x, self.rect.y

