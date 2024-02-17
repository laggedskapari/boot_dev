class Brawler:
    def __init__(self, speed, strength, name):
        self.speed = speed
        self.strength = strength
        self.power = speed * strength
        self.name = name


if __name__ == "__main__":
    brawler_1 = Brawler(4, 4, Aragorn)
    brawler_2 = Brawler(2, 7, Gimli)
    brawler_3 = Brawler(7, 7, Legolas)
    brawler_4 = Brawler(3, 2, Frodo)
