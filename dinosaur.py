

class dinosaur:
    def __init__(self):
        self.name = ''
        self.attack_power = 25
        self.health = 100

    def attack(self, robot):
        self.enemy_robot = robot - self.attack_power
        self.health = self.enemy_robot
        return self.enemy_robot