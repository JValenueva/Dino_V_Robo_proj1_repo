

class dinosaur:
    def __init__(self):
        self.name = 'Riot'
        self.attack_power = 25
        self.health = 100

    def attack(self, robot):
        self.enemy = robot - self.attack_power
        return self.enemy