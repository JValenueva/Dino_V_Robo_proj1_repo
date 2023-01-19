from weapon import weapon
from dinosaur import dinosaur

class robot:
    def __init__(self, name) -> None:
        self.name = name
        self.health = 100
        self.active_weapon = weapon()

    def attack(self):
        self.dinosaur = dinosaur()