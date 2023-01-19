class robot:
    def __init__(self, name, Weapon) -> None:
        self.name = name
        self.health = '100'
        self.active_weapon = Weapon

    def attack(self, dinosaur):
        self.dinosaur = dinosaur