# Untouchable Game with Q-learning Agent

This project showcases the "Untouchable" game implemented in Python using the Pygame library, featuring an integrated Q-learning agent to play the game.
The Q-learning agent is designed to excel in the game by making smart decisions and optimizing its score.

## Features

- "Untouchable" game with a graphical interface.
- Q-learning agent capable of learning and playing the game.
- Option to train the agent or play the game manually.

## Dependencies

Before running the game, ensure you have the following dependencies installed:

- Python 3.11
- Pygame
- Matplotlib
- NumPy

You can install Pygame and Matplotlib using pip:

```bash
pip install pygame matplotlib numpy
```

## Playing the Game
To play "Untouchable" manually, execute the following command:
```bash
python main.py
```

## Performance Visualization
The game monitors the agent's performance over episodes and displays a performance graph at the end of training. You can track the progression of the agent's total score over time.

## Project Structure
main.py: The primary script to launch the game and initiate training.

constants.py: Contains constants and configurations for the game.

button.py: Defines a class for creating in-game buttons.

enemy.py: Defines a class for enemies.

player.py: Defines a class for a player with the controls for actions in the game.

timepack.py: Handles time pack entities.

agent.py: Implements the Q-learning agent.

q_table.npy: Contains the pre-trained Q-table (if available).

## Acknowledgments
The "Untouchable" game was developed as a unique gaming experience. Pygame was used for creating the graphical interface, and the Q-learning algorithm plays a vital role in optimizing agent performance.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
