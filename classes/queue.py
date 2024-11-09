from classes.stack import Stack

# Queue Class
class Queue:
    # Constructor
    def __init__(self):
        self.stock_pile = Stack()
        self.waste_pile = Stack()
        self.size = 0

    # Enqueue card into the queue
    def enqueue(self,card):
        self.size += 1
        self.stock_pile.push(card)
    
    # Removing card from the queue
    def dequeue(self):
        # If waste pile is empty
        if self.waste_pile.is_empty():
            return None

        # If waste pile is empty
        card = self.waste_pile.pop()
        self.size -= 1

        # If after removing card waste pile is not empty flipping the existing cards for showing the cards
        if not self.waste_pile.is_empty():
            self.waste_pile.flip_cards()
        return card
    
    # Drawing card from stock to waste pile
    def draw_card(self):
        # If stock and waste 
        if self.stock_pile.is_empty() and self.waste_pile.is_empty():
            return
        
        if self.stock_pile.is_empty():
            while not self.waste_pile.is_empty():
                self.stock_pile.push(self.waste_pile.pop())
            return
        
        card = self.stock_pile.pop()
        self.waste_pile.push(card)
        self.waste_pile.flip_cards()
    
    # Number of cards in queue
    def cards_count(self):
        return self.size
    
    # Display function to display cards
    def display(self):
        # Displaying stock pile
        print("\nStock Pile:", end=" ")
        if self.stock_pile.is_empty(): print(" No cards available!")
        else: print("Cards available")
        
        # Displaying waste pile
        print("\nWaste Pile:",end=" ")
        if self.waste_pile.is_empty():print("No cards available!")
        else: self.waste_pile.display()

    # Checks if the queue is empty
    def is_empty(self):
        return self.size == 0