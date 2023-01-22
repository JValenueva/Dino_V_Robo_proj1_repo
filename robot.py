from weapon import weapon

class robot:
    def __init__(self):
        self.name = 'Dozer'
        self.health = 100
        self.active_weapon = weapon()

    def attack(self, dinosaur):
        self.enemy = dinosaur - self.active_weapon.attack_power
        self.health = self.enemy
        return self.enemy
        