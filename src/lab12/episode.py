''' 
Lab 12: Beginnings of Reinforcement Learning
We will modularize the code in pygrame_combat.py from lab 11 together.

Then it's your turn!
Create a function called run_episode that takes in two players
and runs a single episode of combat between them. 
As per RL conventions, the function should return a list of tuples
of the form (observation/state, action, reward) for each turn in the episode.
Note that observation/state is a tuple of the form (player1_health, player2_health).
Action is simply the weapon selected by the player.
Reward is the reward for the player for that turn.
'''

from GAME450_CMPSC441_Labs.src.lab11.turn_combat import Combat


def run_episode(player1, player2):
    # Initialize the Combat game instance
    currentGame = Combat()
    episode_history = []

    # Run the combat until the game is over
    while not currentGame.gameOver:
        # Observation before actions are taken
        observation = (player1.health, player2.health)

        # Players select their actions
        player1_action = player1.weapon_selecting_strategy()
        player2_action = player2.weapon_selecting_strategy()

        # Apply the actions and update the game state
        currentGame.takeTurn(player1, player2)
        
        # Compute rewards after the actions
        reward = currentGame.checkWin(player1, player2)  # Simplification for demonstration
        
        # Save the step to the episode history
        episode_history.append((observation, (player1_action, player2_action), reward))

    return episode_history
