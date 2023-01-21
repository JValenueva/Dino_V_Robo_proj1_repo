from Robot import robot
Robot = robot()

class dinosaur:
    def __init__(self):
        self.name = 'Riot'
        self.attack_power = 25
        self.health = 100

    def attack(self):
        print(f'{dinosaur.name} dealt {self.attack_power} to {Robot.name}!')
        self.robot_blow = Robot.health - self.attack_power
        print(f'{Robot.name} has {self.robot_blow} health remaining!')