import pygame
import random
import sys
from pathlib import Path
sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))
from lab11.turn_combat import CombatPlayer
from lab14.lab14 import global_journal  

class PyGameAIPlayer:
    def __init__(self) -> None:
        pass

    def selectAction(self, state):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if ord("0") <= event.key <= ord("9"):
                    return event.key
        
        return ord(str(state.current_city))  # Not a safe operation for >10 cities


class PyGameAICombatPlayer(CombatPlayer):  
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        # Randomly select a weapon
        self.weapon = random.randint(0, 2)  # Choose among 0 (Sword), 1 (Arrow), or 2 (Fire)
        global_journal.generate_text_entry(f"AI decided to use {self.weapon}")
        return self.weapon
