def becomes_warrior(first_name, last_name, power):
    return f"{first_name} {last_name} the warrior", power + 1


if __name__ == "__main__":
    print(becomes_warrior("Padmini", "Sharma", 10))
