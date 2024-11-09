from classes.linkedlist import LinkedList

# Stack Class
class Stack:
    # Constructor
    def __init__(self):
        self.linkedList = LinkedList()
        self.size = 0
    
    # Pushing the card into the stack
    def push(self,card):
        self.size +=1
        self.linkedList.insert_at_head(card)
    
    # Popping the card from stack
    def pop(self):
        # Checks size if greater than 0 it pops the card from the stack
        if self.size -1>=0:
            self.size -=1
            return self.linkedList.remove_from_head()
        return None

    # Viewing the top card in the stack
    def peek(self):
        # If the size of the stack is greater than 0
        if self.size>0:
            return self.linkedList.view_first_node()
        return None
    
    # Number of cards in stack
    def cards_count(self):
        return self.size
    
    # Flipping all cards in the stack
    def flip_cards(self):
        if self.size>0:
            self.linkedList.flip_cards()

    # Display function to display cards
    def display(self):
        self.linkedList.display_elements()

    # Checks if the stack is empty
    def is_empty(self):
        return self.linkedList.is_empty()