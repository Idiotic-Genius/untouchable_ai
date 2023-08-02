import pygame

import constants as const
from enemy import Enemy
from player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (const.SCREEN_WIDTH, const.SCREEN_HEIGHT)
        )
        pygame.display.set_caption(const.GAME_NAME)
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)

        # Create enemies and add them to groups
        for _ in range(8):
            enemy = Enemy()
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

    def run(self):
        # Game loop
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Update the game
            self.all_sprites.update()

            # Check for collisions between the player and enemies
            hits = pygame.sprite.spritecollide(
                self.player, 
                self.enemies, 
                False
                )
            if hits:
                running = False

            # Draw everything
            self.screen.fill(const.BLACK)
            self.all_sprites.draw(self.screen)
            pygame.display.flip()

            # Control the game speed
            pygame.time.delay(30)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
