# card class
class Card:
    # intializing class
    def __init__(self,rank,suit):
        self.rank = rank # rank
        self.suit = suit # suit of the card
        self.faceDown = True # face position on start setting to face down
    
    # function to update the card position
    def updatePostition(self):
        self.faceDown = not self.faceDown
        
    # function to check the card position
    def checkFace(self):
        return self.faceDown
    
    # function to check the card color
    def checkColor(self):
        if self.suit == "Diamonds" or self.suit == "Hearts":
            return "Red"
        else:
            return "Black"