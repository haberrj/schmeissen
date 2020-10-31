import os
import sys
import rando
import itertools import product

class Card(object):
    def __init__(self, rank, suit, value):
        self.rank = rank #string
        self.suit = suit #string 
        self.value = value #int
        self.card = str(self.rank) + " " + str(self.suit)
    
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

class Deck(object):
    def __init__(self):
        self.deck = []
        self.dealt = [] #Prevents from dealing the same card
        self.PopulateDeck()

    def PopulateDeck(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        for suit in suits:
            for rank in range(2, 15):
                if rank == 11:
                    value = "Jack"
                elif rank == 12:
                    value = "Queen"
                elif rank == 13:
                    value = "King"
                elif rank == 14:
                    value = "Ace"
                else:
                    value = str(rank)

                self.deck.append(Card(value, suit, rank))

    def deal(self):
        #Randomly select card
        remaining_cards = [card for card in self.deck if card not in self.dealt]
        try:
            card_index = random.randrange(0, len(remaining_cards)-1)
        except ValueError:
            print("No cards left in the deck!")
            return ""
        card = remaining_cards[card_index]
        self.dealt.append(card)
        return card

    def shuffle(self):
        self.dealt = []