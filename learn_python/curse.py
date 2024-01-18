def curse(weapon_damage):
    lesser_curse = 0.5 * weapon_damage
    greater_curse = 0.25 * weapon_damage
    return lesser_curse, greater_curse


def tests(weapon_damage):
    print(f"Base Damage: {float(weapon_damage)}")
    print("Cursing...")
    lesser_cursed, greater_cursed = curse(weapon_damage)
    print(f"Lesser cursed : {
          lesser_cursed} and Greater cursed : {greater_cursed}")


if __name__ == '__main__':
    tests(100)
    tests(1000)
    tests(200)
