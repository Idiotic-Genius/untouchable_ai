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

    def update(self) -> None:
        action = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            action = const.Directions.LEFT
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            action = const.Directions.RIGHT
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            action = const.Directions.UP
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            action = const.Directions.DOWN
        self.move_player(action=action)

    def move_player(self, action: int) -> None:
        if action == const.Directions.LEFT and self.rect.left > 0:
            self.rect.x -= self.speed
        if action == const.Directions.RIGHT and self.rect.right < const.SCREEN_WIDTH:
            self.rect.x += self.speed
        if action == const.Directions.UP and self.rect.top > 0:
            self.rect.y -= self.speed
        if action == const.Directions.DOWN and self.rect.bottom < const.SCREEN_HEIGHT:
            self.rect.y += self.speed

    def increase_time(self, value: int) -> None:
        self.time += value

    def decrease_time(self, value: int) -> None:
        self.time -= value

    def increase_score(self, value: int) -> None:
        self.score += value

    def get_pos(self) -> tuple[int, int]:
        return self.rect.x, self.rect.y