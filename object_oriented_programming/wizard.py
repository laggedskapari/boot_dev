class Wizard:
    def __init__(self, name, mana, health):
        self.name = name
        self.__mana = 65
        self.__health = 45

    def get_mana(self):
        return self.__mana

    def get_health(self):
        return self.__health

    def get_fireballed(self):
        self.__health -= 30

    def drink_mana_potion(self):
        self.__mana += 40

    def cast_fireball(self, target):
        if (self.__mana > 20):
            self.__mana -= 30
            print(f"{self.name} casts fireball at {self.target}")
            return
        print(f"{self.name} cannot cast fireball")
