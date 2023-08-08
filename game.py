import pygame

import constants as const
from button import Button
from enemy import Enemy
from player import Player
from time_pack import TimePack


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(
            (const.SCREEN_WIDTH, const.SCREEN_HEIGHT)
        )
        pygame.display.set_caption(const.GAME_NAME)

        # Fonts for displaying text
        self.time_font = pygame.font.Font(None, const.FONT_SIZE)
        self.score_font = pygame.font.Font(None, const.FONT_SIZE)

        # Initialize sprites
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.time_packs = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)

        # Create enemies and add them to groups
        for _ in range(const.ENEMY_NUM):
            enemy = Enemy()
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

        # Create time packs and add them to groups
        for _ in range(1):
            time_pack = TimePack()
            self.all_sprites.add(time_pack)
            self.time_packs.add(time_pack)

        # Custom Events
        self.decrement_player_time = pygame.USEREVENT + 1
        pygame.time.set_timer(self.decrement_player_time, 1000)
        self.increase_score = pygame.USEREVENT + 2
        pygame.time.set_timer(self.increase_score, 10)
        self.end_screen_event = pygame.USEREVENT + 3

    def run(self):
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == self.decrement_player_time:
                    self.player.decrease_time(value=1)
                    if self.player.time < 0:
                        running = False
                elif event.type == self.increase_score:
                    self.player.increase_score(value=1)
                elif event.type == self.end_screen_event:
                    self.game_over_screen()

            # Update the game
            self.all_sprites.update()

            # Check for collisions between the player and enemies
            enemy_collisions = pygame.sprite.spritecollide(
                self.player,
                self.enemies,
                False
            )
            if enemy_collisions:
                pygame.event.post(pygame.event.Event(self.end_screen_event))

            # Check for collisions between player and time packs
            time_pack_collisions = pygame.sprite.spritecollide(
                self.player,
                self.time_packs,
                False
            )
            for sprite in time_pack_collisions:
                if isinstance(sprite, TimePack):
                    self.player.increase_time(value=sprite.value)
                    sprite.spawn()

            # Populate text
            time_text = self.time_font.render(
                f'Time remaining: {self.player.time}',
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
            self.screen.blit(score_text, const.SCORE_DISPLAY_LOC)
            self.screen.blit(time_text, const.TIME_DISPLAY_LOC)
            pygame.display.flip()

            # Control the game speed
            pygame.time.delay(const.GAME_SPEED)

        pygame.quit()

    def game_over_screen(self):
        restart_button = Button(
            const.RESTART_BUTTON_LOC,
            const.MENU_BUTTON_WIDTH,
            const.MENU_BUTTON_HEIGHT,
            "Restart"
        )
        quit_button = Button(
            const.QUIT_BUTTON_LOC,
            const.MENU_BUTTON_WIDTH,
            const.MENU_BUTTON_HEIGHT,
            "Quit"
        )

        end_screen = True
        while end_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if restart_button.handle_event(event=event):
                    end_screen = False
                    self.__init__()
                if quit_button.handle_event(event=event):
                    pygame.quit()

            score_text = self.time_font.render(
                f'score: {self.player.score}',
                True,
                const.WHITE
            )
            self.screen.fill(const.BLACK)
            self.screen.blit(score_text, const.SCORE_DISPLAY_LOC)
            restart_button.draw(screen=self.screen)
            quit_button.draw(screen=self.screen)
            pygame.display.flip()

            pygame.time.delay(const.GAME_SPEED)


if __name__ == "__main__":
    game = Game()
    game.run()
