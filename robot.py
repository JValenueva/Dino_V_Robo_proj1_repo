from weapon import weapon

class robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = weapon('spear', 25)

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        
        