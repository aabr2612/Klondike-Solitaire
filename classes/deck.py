import random
from classes.card import Card

# Deck Class
class Deck:
    # Constructor
    def __init__(self):
        self.cards = [] # Array to hold the cards
        self.loadCards() # Function to load the cards
        self.shuffle_cards_randomly() # Function to shuffle the cards when deck is once made

    # Loading the cards for the deck
    def loadCards(self):
        suits = ["Diamonds", "Hearts", "Spades", "Clubs"] # Suits
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"] # Ranks
        
        # Loading card one by one for suits according to ranks
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.cards.append(card)

    # Using random function to shuffle cards randomly
    def shuffle_cards_randomly(self):
        random.shuffle(self.cards)

    # Function to draw a card
    def draw_card(self):
        # If cards are present in the deck
        if self.cards:
            return self.cards.pop()
        
        # If deck is empty
        print("No more cards to draw!")
        return None

    # Function to display all cards of the deck
    def display(self):
        i = 1
        # Displaying each card's rank and suit
        for card in self.cards:
            print(card.suit + " " + str(card.rank), end=" -> ")
            if i % 13 == 0:
                print()
            i += 1