# Card Class
class Card:
    # Constructor
    def __init__(self,rank,suit):
        self.rank = rank # Rank of card
        self.suit = suit # Suit of card
        self.name = self.card_name() # Giving card a short name to compare for easy movements
        self.face_down = True # Face position of card
    
    # Function to assign card a name
    def card_name(self):
        ranks = {"Ace":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"Jack":11,"Queen":12,"King":13}
        return str(ranks[self.rank])+self.suit[0]
    
    # Redefining str function for card display
    def __str__(self):
        return f"{self.rank} of {self.suit} [{self.name}]"
    
    # Flip card position
    def flip_card(self):
        self.face_down = not self.face_down
    
    # Check if card is lower than this one
    def check_rank_lower(self,source_card):
        ranks = {"Ace":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"Jack":11,"Queen":12,"King":13}
        return ranks[self.rank] == ranks[source_card.rank]+1
    
    # Checking the color of the card
    def check_card_color(self):
        return "Red" if self.suit in ["Diamonds","Hearts"] else "Black"