from Robot import robot
from Dinosaur import dinosaur


class battlefield:
    def __init__(self):
        self.Robot = robot('brother bot')
        self.Dinosaur = dinosaur('ancient', 25)
    
    def run_game(self):
        battlefield.display_welcome(self)
        print(f'{self.Robot.name} will have first move on the battlefield!')
        battlefield.battle_phase(self)
        battlefield.display_winner(self)

    def display_welcome(self):
        print('Welcome to Robots vs. Dinosaurs Simulator')
        print(f'Our first match of the night pits {self.Robot.name} against {self.Dinosaur.name}!')

    def battle_phase(self):
        while self.Dinosaur.health or self.Robot.health >= 0:
            self.Robot.attack(self.Dinosaur.health)
            self.Dinosaur.attack(self.Robot.health)
            if self.Dinosaur.health <= 0:
                print(f'{self.Dinosaur.name} has fallen to {self.Robot.name}!')
                break
            elif self.Robot.health <= 0:
                print(f'{self.Robot.name} has fallen to {self.Dinosaur.name}!')
                break

    def display_winner(self):
        if self.Dinosaur.health <= 0:
            print(f'The last one standing on the battlefield is {self.Dinosaur.name}!')
        elif self.Robot.health <= 0:
            print(f'The last one standing on the battlefield is {self.Robot.name}!')