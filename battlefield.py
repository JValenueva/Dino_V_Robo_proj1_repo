from Robot import robot
from Dinosaur import dinosaur

class battlefield:
    def __init__(self):
        self.Robot = robot()
        self.Dinosaur = dinosaur()
        
    def display_welcome(self):
        print('Welcome to Robots vs. Dinosaurs Simulator')
        print(f'Our first match of the night pits {self.Robot.name} against {self.Dinosaur.name}!')

    def run_game(self):
        print(f'{self.Robot.name} will have first move on the battlefield!')
        while self.Dinosaur.health or self.Robot.health != 0:
            battlefield.battle_phase
        
    def battle_phase(self):
        self.Robot.attack(self.Dinosaur.health)
        print(f'{self.Robot.name} dealt {self.Robot.active_weapon.attack_power} damage to {self.Dinosaur.name} with {self.Robot.active_weapon.name}!')
        self.Dinosaur.attack
        print(f'{self.Dinosaur.name} dealt {self.Dinosaur.attack_power} damage to {self.Robot.name}!')

    def display_winner(self):
        if self.Dinosaur.health == 0:
            print(f'The last one standing on the battlefield is {self.Dinosaur.name}!')
        elif self.Robot.health == 0:
            print(f'The last one standing on the battlefield is {self.Robot.name}!')