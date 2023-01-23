from Robot import robot
from Dinosaur import dinosaur


class battlefield:
    def __init__(self, robot_name, dinosaur_name, robot_weapon_name):
        self.Robot = robot()
        self.Dinosaur = dinosaur()
        self.Robot.name = robot_name
        self.Dinosaur.name = dinosaur_name
        self.Robot.active_weapon.name = robot_weapon_name
    
    def run_game(self):
        print(f'{self.Robot.name} will have first move on the battlefield!')
        
        while self.Robot.health or self.Dinosaur.health != 0:
            self.Robot.attack(self.Dinosaur.health)
            print(f'{self.Robot.name} dealt {self.Robot.active_weapon.attack_power} damage to {self.Dinosaur.name} with {self.Robot.active_weapon.name}!')
            print(' ')
            print(f'{self.Dinosaur.name} has {self.Dinosaur.health} health remaining!')
           
            self.Dinosaur.attack(self.Robot.health)
            print(f'{self.Dinosaur.name} dealt {self.Dinosaur.attack_power} damage to {self.Robot.name}!')
            print(' ')
            print(f'{self.Robot.name} has {self.Robot.health} remaining!')
            if self.Dinosaur.health <= 0:
                print(f'Fatality! {self.Dinosaur.name} wins!')
                break
            elif self.Robot.health <= 0:
                print(f'Fatality! {self.Robot.name} wins!')
                break

    def display_welcome(self):
        print('Welcome to Robots vs. Dinosaurs Simulator')
        print(f'Our first match of the night pits {self.Robot.name} against {self.Dinosaur.name}!')

    def battle_phase(self):
        pass
        
            
    def display_winner(self):
        if self.Dinosaur.health <= 0:
            print(f'The last one standing on the battlefield is {self.Dinosaur.name}!')
        elif self.Robot.health <= 0:
            print(f'The last one standing on the battlefield is {self.Robot.name}!')