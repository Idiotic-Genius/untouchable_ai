import numpy as np
from typing import Optional


class QLearningAgent:
    def __init__(
        self,
        num_states: int,
        num_actions: int,
        learning_rate: float,
        discount_factor: float,
        exploration_rate: float,
        q_table: Optional[np.ndarray] = None
    ) -> None:
        self.num_states = num_states
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        if q_table is not None:
            self.q_table = q_table
        else:
            self.q_table = np.zeros((num_states, num_actions))

    def select_action(
        self,
        state: int
    ) -> int:
        if np.random.rand() < self.exploration_rate:
            return np.random.choice(self.num_actions)
        else:
            return np.argmax(self.q_table[state, :])

    def update_q_value(
        self,
        state: int,
        action: int,
        reward: float,
        next_state: int
    ) -> None:
        best_next_action = np.argmax(self.q_table[next_state, :])
        self.q_table[state, action] = (
            (1 - self.learning_rate) * self.q_table[state, action]
            + self.learning_rate * (
                reward + self.discount_factor * self.q_table[next_state, best_next_action]
            )
        )
