from Robot import robot
from Dinosaur import dinosaur


class battlefield:
    def __init__(self):
        self.Robot = robot('brother bot')
        self.Dinosaur = dinosaur('ancient', 25)
        pass

    def run_game(self):
        self.display_welcome()
        print(f'{self.Robot.name} will have first move on the battlefield!')
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('Welcome to Robots vs. Dinosaurs Simulator')
        print(f'Our first match of the night pits {self.Robot.name} against {self.Dinosaur.name}!')

    def battle_phase(self):
        while self.Dinosaur.health >= 0 and self.Robot.health >= 0:
            self.Robot.attack(self.Dinosaur)

            print(f'{self.Robot.name} attacks with {self.Robot.active_weapon.name} and deals {self.Robot.active_weapon.attack_power} damage!')
            print(f'{self.Dinosaur.name} has {self.Dinosaur.health} left!')
            print(' ')

            self.Dinosaur.attack(self.Robot)
            print(f'{self.Dinosaur.name} landed a blow on {self.Robot.name} and dealt {self.Dinosaur.attack_power} damage!')
            print(f'{self.Robot.name} has {self.Robot.health} remaining!')
            print(' ')

            if self.Dinosaur.health == 0:
                print(f'{self.Dinosaur.name} has fallen to {self.Robot.name}!')
                break
            elif self.Robot.health == 0:
                print(f'{self.Robot.name} has fallen to {self.Dinosaur.name}!')
                break

    def display_winner(self):
        if self.Dinosaur.health == 0:
            print(f'The last one standing on the battlefield is {self.Dinosaur.name}!')
        elif self.Robot.health == 0:
            print(f'The last one standing on the battlefield is {self.Robot.name}!')