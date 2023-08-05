import pygame

import constants as const
from enemy import Enemy
from player import Player



class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(
            (const.SCREEN_WIDTH, const.SCREEN_HEIGHT)
        )
        pygame.display.set_caption(const.GAME_NAME)

        # Fonts for displaying text
        self.life_font = pygame.font.Font(None, 36)

        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)

        # Create enemies and add them to groups
        for _ in range(25):
            enemy = Enemy()
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

        # Custom Events
        self.decrement_player_life = pygame.USEREVENT + 1
        pygame.time.set_timer(self.decrement_player_life, 1000)
        self.increase_player_life = pygame.USEREVENT + 2

    def run(self):
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == self.decrement_player_life:
                    self.player.life -= 1
                    if self.player.life < 0:
                        running = False
                if event.type == self.increase_player_life:
                    pass

            # Update the game
            self.all_sprites.update()

            # Check for collisions between the player and enemies
            hits = pygame.sprite.spritecollide(
                self.player,
                self.enemies,
                False
            )
            if hits:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

            # Check for collisions between player and life packs

            # Populate text
            life_text = self.life_font.render(
                f'Life remaining: {self.player.life}',
                True,
                const.WHITE
            )

            # Draw everything
            self.screen.fill(const.BLACK)
            self.all_sprites.draw(self.screen)
            self.screen.blit(life_text, const.SCORE_LOCATION)
            self.screen.blit(life_text, const.LIFE_LOCATION)
            pygame.display.flip()

            # Control the game speed
            pygame.time.delay(const.GAME_SPEED)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
