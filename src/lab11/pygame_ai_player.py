import pygame
import random
from pygame_human_player import PyGameHumanCombatPlayer  
from turn_combat import CombatPlayer  
class PyGameAIPlayer:
    def __init__(self, number_of_cities) -> None:
        self.number_of_cities = number_of_cities

    def selectAction(self, state):
        if state.travelling:
            return 48  # ASCII code for 0, meaning "keep going"
        else:
            # Selecting a random city that is not the current one
            return ord(str((state.current_city + random.randint(1, self.number_of_cities - 1)) % self.number_of_cities))

class PyGameAICombatPlayer(PyGameHumanCombatPlayer):  
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        # Randomly select a weapon
        self.weapon = random.randint(0, 2)  # Choose among 0 (Sword), 1 (Arrow), or 2 (Fire)
        return self.weapon
