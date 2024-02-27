import random

SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'King', 'Ace']


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):
        return RANKS.index(self.rank) < RANKS.index(other.rank) or SUITS.index(self.suit) < SUITS.index(other.suit)

    def __gt__(self, other):
        return RANKS.index(self.rank) > RANKS.index(other.rank) or SUITS.index(self.suit) > SUITS.index(other.suit)
