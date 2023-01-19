from robot import robot
from dinosaur import dinosaur
from weapon import weapon

class battlefield:
    def __init__(self):
        self.Robot = robot()
        self.Dinosaur = dinosaur()
        
    def display_welcome(self):
        print('Welcome to Robots vs. Dinosaurs Simulator')
    
    def battle_phase(self):

    def display_winner(self):
        if self.Dinosaur.health == 0:
            print(f'The last one standing on the battlefield is {self.Dinosaur.name}!')
        elif self.Robot.health == 0:
            print(f'The last one standing on the battlefield is {self.Robot.name}!')
    
    def run_game(self):
        