def get_punched(health, armour=0):
    return health - abs(armour - 50)


def get_slashed(health, armour=0):
    return health - abs(armour - 100)


if __name__ == "__main__":
    health = 400
    health = get_punched(health, 0)
    health = get_slashed(health, 100)
    print(health)
