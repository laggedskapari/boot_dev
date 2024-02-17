class Archer:
    def __init__(self, name, health, num_arrows):
        self.name = name
        self.health = health
        self.num_arrow = num_arrows

    def get_shot(self):
        if (self.health <= 0):
            print(f"{self.name} is dead")
            return
        self.health -= 1

    def shoot(self, target):
        if (self.num_arrow <= 0):
            print(f"{self.name} can't shoot")
            return
        self.num_arrow -= 1
        print(f"{self.name} shoots {target}")



