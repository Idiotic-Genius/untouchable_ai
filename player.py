import pygame

import constants as const


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface(const.PLAYER_SIZE)
        self.image.fill(const.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = const.SCREEN_CENTER_POS
        self.speed = const.PLAYER_SPEED
        self.time = const.PLAYER_STARTING_TIME
        self.score = 0
        self.packs_eaten = 0

    def update(self) -> None:
        action = 0
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left > 0:
            action = const.Directions.LEFT.value
            self.move_player(action=action)
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right < const.SCREEN_WIDTH:
            action = const.Directions.RIGHT.value
            self.move_player(action=action)
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.rect.top > 0:
            action = const.Directions.UP.value
            self.move_player(action=action)
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.rect.bottom < const.SCREEN_HEIGHT:
            action = const.Directions.DOWN.value
            self.move_player(action=action)

    def move_player(self, action: int) -> None:
        if action == const.Directions.LEFT.value and self.rect.left > 0:
            self.rect.x -= self.speed
        if action == const.Directions.RIGHT.value and self.rect.right < const.SCREEN_WIDTH:
            self.rect.x += self.speed
        if action == const.Directions.UP.value and self.rect.top > 0:
            self.rect.y -= self.speed
        if action == const.Directions.DOWN.value and self.rect.bottom < const.SCREEN_HEIGHT:
            self.rect.y += self.speed

    def increase_time(self, value: int) -> None:
        self.time += value

    def decrease_time(self, value: int) -> None:
        self.time -= value

    def increase_score(self, value: int) -> None:
        self.score += value

    def add_packs_eaten(self, value:int) -> None:
        self.packs_eaten += value

    def get_pos(self) -> tuple[int, int]:
        return self.rect.x, self.rect.y
