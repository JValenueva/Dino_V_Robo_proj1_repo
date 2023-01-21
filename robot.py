from Dinosaur import dinosaur
from weapon import weapon
Dinosaur = dinosaur()

class robot:
    def __init__(self):
        self.name = 'Dozer'
        self.health = 100
        self.active_weapon = weapon()

    def attack(self):
        print(f'{robot.name} has dealt {self.active_weapon.attack_power} to {Dinosaur.name}!')
        self.dinosaur_blow = Dinosaur.health - self.active_weapon.attack_power
        print(f'{Dinosaur.name} has {self.dinosaur_blow} health remaining!')