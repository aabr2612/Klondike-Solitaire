import sys
import os
import random

# setting paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BL.card_bl import Card

# deck class
class Deck:
    # initializing deck
    def __init__(self):
        self.cards = [] # array to hold the cards
        self.loadCards() # function to load the cards
        self.shuffleCardsRandomly() # function to shuffle the cards when deck is once made

    # loading the cards for the deck
    def loadCards(self):
        suits = ["Diamonds", "Hearts", "Spades", "Clubs"] # suits
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"] # ranks
        
        # loading card one by one for suits according to ranks
        for suit in suits:
            i = 1
            for _ in ranks:
                card = Card(i, suit)
                self.cards.append(card)
                i += 1

    # using random function to shuffle cards randomly
    def shuffleCardsRandomly(self):
        random.shuffle(self.cards)

    # function to draw a card
    def drawCard(self):
        if self.cards:
            return self.cards.pop()
        else:
            print("No more cards to draw!")
            return None

    # function to reset the current deck so that same deck can be updated and used again
    def resetDeck(self):
        self.cards.clear() # clearing the cards
        self.loadCards() # loading the cards again
        self.shuffleCardsRandomly() # shuffling cards

    # function to display all cards
    def display(self):
        i = 1
        for card in self.cards:
            print(card.suit + "   " + str(card.rank), end=" -> ")
            if i % 13 == 0:
                print()
            i += 1