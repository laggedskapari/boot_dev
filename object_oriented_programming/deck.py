import random


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.__cards = []
        self.__cards = self.create_deck()

    def create_deck(self):
        for rank, suit in self.RANKS, self.SUITS:
            self.__cards.append(tuple(rank, suit))

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        self.__cards.pop()
    # don't touch below this line

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"
