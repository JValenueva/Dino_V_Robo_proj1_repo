from weapon import weapon

class robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = weapon('spear', 30)

    def attack(self, dinosaur):
        self.enemy_dinosaur = dinosaur
        self.enemy_dinosaur -= self.active_weapon.attack_power
        
        