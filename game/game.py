from classes.stack import Stack
from classes.deck import Deck
from classes.queue import Queue

# Game Class
class Game:
    # Constructor
    def __init__(self):
        self.tableau=[Stack() for _ in range(7)] # Initializing tableau
        self.foundation=[Stack() for _ in range(4)] # Initalizing foundations
        self.deck = Deck() # Initializing deck
        self.stock_pile = Queue() # Stock pile
        self.initialize_game() # Initializing game
    
    # Game initialization
    def initialize_game(self):
        # Pushing cards into tableau
        for i in range(7):
            for j in range(i+1):
                card = self.deck.draw_card()
                if card:
                    if j==i:
                        card.flip_card()
                    self.tableau[i].push(card)
        
        card = self.deck.draw_card()
        # Pushing cards into stockpile from deck
        while card:
            self.stock_pile.enqueue(card)
            card=self.deck.draw_card()

    # Displaying current game state
    def display(self):
        # Displaying tableau
        print("\nTableau:\n")
        for i in range(7):
            print("Tableau "+str(i+1)+":",end=" ")
            self.tableau[i].display()
            
        # Displaying Foundation
        print("\nFoundations:\n")
        for i in range(4):
            print("Foundation "+str(i+1)+":",end=" ")
            self.foundation[i].display()
        
        # Displaying stock and waste
        self.stock_pile.display()
    
    # Drawing card from stock to waste pile
    def draw_card_from_stockpile(self):
        self.stock_pile.draw_card()
    
    def move_card_from_waste(self):
        self.tableau[0].push(self.tableau[6].pop())
        return self.stock_pile.dequeue()