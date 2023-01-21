from Robot import robot
from Dinosaur import dinosaur
list_1 = ['robot', 'dinosaur']

class battlefield:
    def __init__(self):
        self.Robot = robot()
        self.Dinosaur = dinosaur()
        
    def display_welcome(self):
        print('Welcome to Robots vs. Dinosaurs Simulator')

    def run_game_1(self):
        import random
        random.choice(list_1)
        return random
    verdict = run_game_1(list_1)

    def run_game(self, verdict):
        if verdict == 'robot':
            print(f'{self.Robot.name} will have first move on the battlefield!')
            while self.Dinosaur.health != 0:
                self.Robot.attack
        elif verdict == 'dinosaur':
            print(f'{self.Dinosaur.name} will have the first move on the battlefield!')
            while self.Robot.health != 0:
                self.Dinosaur.attack
        
        
    def battle_phase(self):
        self.Dinosaur.health

    def display_winner(self):
        if self.Dinosaur.health == 0:
            print(f'The last one standing on the battlefield is {self.Dinosaur.name}!')
        elif self.Robot.health == 0:
            print(f'The last one standing on the battlefield is {self.Robot.name}!')