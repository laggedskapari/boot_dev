class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage


class Archer(Hero):
    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.__num_arrows = num_arrows

    def shoot(self, target):
        if self.__num_arrows < 0:
            raise ValueError("Not enought arrows")
        target.take_damage(10)


class Wizard(Hero):
    def __init__(self, name, health, mana):
        super.__init__(name, health)
        self.__mana = mana

    def cast(self, target):
        if self.__mana < 25:
            raise ValueError("Not enough mana")
        target.take_damage(25)
        self.__mana -= 25
