# Node Class
class Node:
    # Constructor
    def __init__(self,card):
        self.card = card # Card
        self.next = None # Next

# LinkedList Class
class LinkedList:
    # Constructor
    def __init__(self):
        self.head = None

    # Function to insert element at the head
    def insert_at_head(self,card):
        new_node = Node(card)

        # If the head is none then set the new node as head
        if self.is_empty():
            self.head = new_node

        # If head already present then set the new node as head and set its next to previous head
        else:
            new_node.next=self.head
            self.head = new_node
        
    # Function to remove element from the head
    def remove_from_head(self):
        
        # If linkedlist is empty
        if self.is_empty():
            print("No more cards!")
            return None
        
        # If head is the only element in the linkedlist set the head none to indicate that the linkedlist is empty
        if self.head.next==None:
            temp = self.head
            self.head=None
            return temp.card
        
        # If head is not empty removing card from it
        temp = self.head
        self.head = self.head.next
        
        # Flipping the head card
        if self.head.card.face_down:
            self.head.card.flip_card()
        return temp.card
    
    # Function to display elements in reversed order
    def display_elements(self):
        # If the linkedlist it empty
        if self.is_empty():
            print()
            return

        # Temporary array of the cards
        cards_array = []
        current = self.head

        # Appending the cards into the array
        while current:
            cards_array.append(current.card)
            current = current.next
        
        # Popping and then printing each element so that the cards are printed in correct order
        while cards_array:
            card = cards_array.pop()
            
            # If card is found
            if card is not None:
                # If card is face down prints face down for the card
                if card.face_down:
                    print("Face-Down", end=" -> ")
                # If card is face up it prints card's rank and suit
                else:
                    print(str(card),end=" -> ")
                    
            # If card not found it breaks the loop
            else:
                break
        
        print()

    # Checks if linkedlist is empty
    def is_empty(self):
        return self.head==None
    
    # Check first node function
    def view_first_node(self):
        
        # If list is empty
        if self.is_empty():
            return None

        # Return the head
        return self.head.card
    
    def find_node(self,card_name):
        # If list is empty
        if self.is_empty():
            return None

        # If list is not empty
        current = self.head
        # Loop continues till a specific card is found else returns none
        while current:
            if  current.card.name==card_name: # If card name of card being compared is equal to card to be searched and the card is visible
                return current.card
            current = current.next
        return None # Return none in case of card not found in the list

    def flip_cards(self):
        # If the linkedlist is empty
        if self.is_empty():
            return

        # Flipping the card's position so that only the first card is visible
        current = self.head
        while current:
            # If currently the card has a face up then it flips it
            if not current.card.face_down:
                current.card.flip_card()
            current = current.next
        
        # Flipping the head of the linkedlist to ensure that the top card is visible
        self.head.card.flip_card()