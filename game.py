import pygame

import constants as const
from enemy import Enemy
from player import Player
from life_pack import LifePack



class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(
            (const.SCREEN_WIDTH, const.SCREEN_HEIGHT)
        )
        pygame.display.set_caption(const.GAME_NAME)

        # Fonts for displaying text
        self.life_font = pygame.font.Font(None, const.FONT_SIZE)
        self.score_font = pygame.font.Font(None, const.FONT_SIZE)

        # Initialize sprites
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.life_packs = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)

        # Create enemies and add them to groups
        for _ in range(25):
            enemy = Enemy()
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

        # Create life packs and add them to groups
        for _ in range(1):
            life_pack = LifePack()
            self.all_sprites.add(life_pack)
            self.life_packs.add(life_pack)

        # Custom Events
        self.decrement_player_life = pygame.USEREVENT + 1
        pygame.time.set_timer(self.decrement_player_life, 1000)
        self.increase_score = pygame.USEREVENT + 2
        pygame.time.set_timer(self.increase_score, 10)

    def run(self):
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == self.decrement_player_life:
                    self.player.decrease_life(value=1)
                    if self.player.life < 0:
                        running = False
                if event.type == self.increase_score:
                    self.player.increase_score(value=1)

            # Update the game
            self.all_sprites.update()

            # Check for collisions between the player and enemies
            enemy_collisions = pygame.sprite.spritecollide(
                self.player,
                self.enemies,
                False
            )
            if enemy_collisions:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

            # Check for collisions between player and life packs
            life_pack_collisions = pygame.sprite.spritecollide(
                self.player,
                self.life_packs,
                False
            )
            for sprite in life_pack_collisions:
                if isinstance(sprite, LifePack):
                    self.player.increase_life(value=sprite.value)
                    sprite.spawn()

            # Populate text
            life_text = self.life_font.render(
                f'Life remaining: {self.player.life}',
                True,
                const.WHITE
            )
            score_text = self.score_font.render(
                f'Score: {self.player.score}',
                True,
                const.WHITE
            )

            # Draw everything
            self.screen.fill(const.BLACK)
            self.all_sprites.draw(self.screen)
            self.screen.blit(score_text, const.SCORE_DISPLAY_LOCATION)
            self.screen.blit(life_text, const.LIFE_DISPLAY_LOCATION)
            pygame.display.flip()

            # Control the game speed
            pygame.time.delay(const.GAME_SPEED)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
