from robot import robot
from dinosaur import dinosaur
list_1 = ['robot', 'dinosaur']

class battlefield:
    def __init__(self):
        self.Robot = robot()
        self.Dinosaur = dinosaur()
        
    def display_welcome(self):
        print('Welcome to Robots vs. Dinosaurs Simulator')

    def run_game(self):
        import random
        first_pick = random.choice(list_1)
        if first_pick == 'robot':
            print(f'{self.Robot.name} will have first move on the battlefield!')
        elif first_pick == 'dinosaur':
            print(f'{self.Dinosaur.name} will have the first move on the battlefield!')
        
        
    def battle_phase(self):
        self.Dinosaur.health

    def display_winner(self):
        if self.Dinosaur.health == 0:
            print(f'The last one standing on the battlefield is {self.Dinosaur.name}!')
        elif self.Robot.health == 0:
            print(f'The last one standing on the battlefield is {self.Robot.name}!')