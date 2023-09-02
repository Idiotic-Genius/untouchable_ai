import pygame
import math
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Optional

import constants as const
from button import Button
from enemy import Enemy
from player import Player
from timepack import TimePack
from agent import QLearningAgent


class Game:
    def __init__(self,
        train_ai: bool,
        agent: Optional[QLearningAgent] = None
    ) -> None:
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(
            (const.SCREEN_WIDTH, const.SCREEN_HEIGHT)
        )
        pygame.display.set_caption(const.GAME_NAME)

        # Setup the game clock
        self.clock = pygame.time.Clock()

        # Fonts for displaying text
        self.time_font = pygame.font.Font(None, const.FONT_SIZE)
        self.score_font = pygame.font.Font(None, const.FONT_SIZE)

        # Q-Learning agent
        self.train_ai = train_ai
        self.agent = agent

        # Initialize sprites
        self.interactable_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.time_packs = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.GroupSingle()
        self.player = Player()
        self.player_sprite.add(self.player)

        # Create enemies and add them to groups
        for _ in range(const.ENEMY_NUM):
            enemy = Enemy()
            self.interactable_sprites.add(enemy)
            self.enemies.add(enemy)

        # Create time packs and add them to groups
        for _ in range(const.TIMEPACK_NUM):
            time_pack = TimePack()
            self.interactable_sprites.add(time_pack)
            self.time_packs.add(time_pack)

        # Custom Events
        self.decrement_player_time = pygame.USEREVENT + 1
        pygame.time.set_timer(self.decrement_player_time, 10)
        self.increase_score = pygame.USEREVENT + 2
        pygame.time.set_timer(self.increase_score, 10)
        self.end_screen_event = pygame.USEREVENT + 3

    def get_game_state(self) -> int:
        # Get the positions of all entities on the screen
        player_x, player_y = self.player.get_pos()
        game_state = player_y * const.SCREEN_WIDTH + player_x
        for sprite in self.interactable_sprites:
            sprite_x, sprite_y = sprite.get_pos()
            sprite_state = sprite_y * const.SCREEN_WIDTH + sprite_x
            game_state += sprite_state

        # Get the time left for the game
        game_state += self.player.time

        return game_state

    def run(self) -> int:
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == self.decrement_player_time:
                    self.player.decrease_time(value=1)
                    if self.player.time <= 0:
                        if self.train_ai:
                            running = False
                        else:
                            self.game_over_screen()
                elif event.type == self.increase_score:
                    self.player.increase_score(value=1)
                elif event.type == self.end_screen_event:
                    self.game_over_screen()

            # Update the game
            if self.train_ai:
                # Get the current state of the game for agent to select action
                current_state = self.get_game_state()
                action = self.agent.select_action(state=current_state)
                self.player.move_player(action=action)
            else:
                self.player_sprite.update()
            self.interactable_sprites.update()

            # Check for collisions between the player and enemies
            enemy_collisions = pygame.sprite.spritecollide(
                self.player,
                self.enemies,
                False
            )
            if enemy_collisions:
                if self.train_ai:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                else:
                    pygame.event.post(pygame.event.Event(self.end_screen_event))

            # Check for collisions between player and time packs
            time_pack_collisions = pygame.sprite.spritecollide(
                self.player,
                self.time_packs,
                False
            )
            if time_pack_collisions:
                for time_pack in time_pack_collisions:
                    self.player.increase_time(value=time_pack.value)
                    time_pack.spawn()

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

            # Update the Q-value
            if self.train_ai:
                player_x, player_y = self.player.get_pos()
                # FIXME: This will break when there is more than one timepack
                for timepack in self.time_packs:
                    timepack_x, timepack_y = timepack.get_pos()
                dist = math.dist(
                    [player_x, player_y],
                    [timepack_x, timepack_y]
                )
                reward = -dist
                if time_pack_collisions:
                    reward += 999
                if self.player.time <= 1:
                    reward -= 999
                next_state = self.get_game_state()
                self.agent.update_q_value(
                    state=current_state,
                    action=action,
                    reward=reward,
                    next_state=next_state
                )

            # Draw everything
            self.screen.fill(const.BLACK)
            self.interactable_sprites.draw(self.screen)
            self.player_sprite.draw(self.screen)
            self.screen.blit(score_text, const.SCORE_DISPLAY_LOC)
            self.screen.blit(time_text, const.TIME_DISPLAY_LOC)
            pygame.display.flip()

            # Control the game speed
            self.clock.tick(const.GAME_SPEED)

        # if not self.train_ai:
        #     pygame.quit()
        return self.player.score

    def game_over_screen(self) -> None:
        # Buttons
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
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if restart_button.handle_event(event=event):
                    end_screen = False
                    self.__init__(train_ai=self.train_ai)
                if quit_button.handle_event(event=event):
                    pygame.quit()

            # Populate text
            score_text = self.time_font.render(
                f'score: {self.player.score}',
                True,
                const.WHITE
            )

            # Draw everything
            self.screen.fill(const.BLACK)
            self.screen.blit(score_text, const.SCORE_DISPLAY_LOC)
            restart_button.draw(screen=self.screen)
            quit_button.draw(screen=self.screen)
            pygame.display.flip()

            # Control the game speed
            self.clock.tick(const.GAME_SPEED)


if __name__ == "__main__":
    # Load Q-Table if one exist TODO: make actual check
    # q_table_file = Path.cwd() / "q_table.npy"
    # q_table = np.load(q_table_file)

    # Initialize the Q-learning agent
    agent = QLearningAgent(
        num_states=const.NUM_STATES,
        num_actions=const.NUM_ACTIONS,
        learning_rate=const.LEARNING_RATE,
        discount_factor=const.DISCOUNT_FACTOR,
        exploration_rate=const.EXPLORATION_RATE,
        # q_table=q_table
    )

    # Initialize the Game
    game = Game(train_ai=True)

    # Performance tracking
    num_episodes = 1000
    episode_rewards = []
    rewards_average = []
    for episode in range(num_episodes):
        game.__init__(train_ai=True, agent=agent)
        reward = game.run()
        episode_rewards.append(reward)
        rewards_average.append(sum(episode_rewards)/len(episode_rewards))
        # Print episode information
        print(f"Episode {episode + 1}/{num_episodes} - Score: {reward}")

    # Save Q-Table
    save_file = Path.cwd() / "q_table"
    np.save(save_file, agent.q_table)

    # Visualization of performance
    plt.plot(episode_rewards, 'k-', label='Episode Score')
    plt.plot(rewards_average, 'r-', label='Running Average')
    plt.xlabel("Episode")
    plt.ylabel("Total Score")
    plt.grid(linestyle=':')
    plt.legend(loc='upper left')
    plt.title("Agent's Performance Over Episodes")
    plt.show()
