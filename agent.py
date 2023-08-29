import numpy as np

class QLearningAgent:
    def __init__(
            self,
            num_states: int,
            num_actions: int,
            learning_rate: float,
            discount_factor: float,
            exploration_prob: float
        ) -> None:
            self.num_states = num_states
            self.num_actions = num_actions
            self.learning_rate = learning_rate
            self.discount_factor = discount_factor
            self.exploration_prob = exploration_prob

            self.q_table = np.zeros((num_states, num_actions))

    def select_action(self, state):
        if np.random.rand() < self.exploration_prob:
            return np.random.choice(self.num_actions)
        else:
            return np.argmax(self.q_table[state, :])

    def update_q_value(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state, :])
        self.q_table[state, action] += self.learning_rate * (
            reward + self.discount_factor * self.q_table[next_state, best_next_action]
            - self.q_table[state, action]
        )
