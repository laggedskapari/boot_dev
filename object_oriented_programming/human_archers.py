class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Archer(Human):
    def __init__(self, name, num_of_arrows):
        super.__init__(name)
        self.__num_of_arrows = num_of_arrows

    def get_arrows(self):
        return self.__num_of_arrows

    def use_arrows(self, num):
        if self.__num_of_arrows < num:
            raise ValueError("Not enough arrows.")
        self.__num_of_arrows -= num


class Crossbowmen(Archer):
    def __init__(self, name, num_arrows):
        super.__init__(name, num_arrows)

    def triple_shot(self, target):
        self.use_arrows(3)
        print(f"{target} was shot with 3 arrows")
