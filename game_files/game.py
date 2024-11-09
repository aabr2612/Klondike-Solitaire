from classes.stack import Stack
from classes.deck import Deck
from classes.queue import Queue
import game_files.utility

# Game Class
class Game:
    # Constructor
    def __init__(self):
        self.tableau=[Stack() for _ in range(7)] # Initializing tableau
        self.foundation=[Stack() for _ in range(4)] # Initalizing foundations
        self.deck = Deck() # Initializing deck
        self.stock_pile = Queue() # Stock pile
        self.initialize_game() # Initializing game
        self.count = 0 # Count to keep a track of the moves
    
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

    # Move card functionality
    def move_card(self,source,destination,source_index,destination_index):
        try:
            # Capitalizing the source and destination keywords to ensure valid comparison
            source = source.capitalize()
            destination = destination.capitalize()
            
            # Checks for source and destination movements and indexes
            if not game_files.utility.validate_movement(source,destination,source_index,destination_index):
                return "Invalid movements! "

            source_index = int(source_index)-1
            destination_index = int(destination_index)-1

            # If the card being moved is from tableau to tableau
            if source == "T" and destination=="T":
                # If the movement is valid
                if self.valid_tableau_to_tableau_move(source_index,destination_index):
                    msg = f"Card moved {str(self.tableau[source_index].peek())} ---> {str(self.tableau[destination_index].peek())} "
                    self.tableau[destination_index].push(self.tableau[source_index].pop())
                    self.count+=1
                    return msg

            # If the card being moved is from tableau to foundation
            if source == "T" and destination=="F":
                # If the movement is valid
                if self.valid_tableau_to_foundation_move(source_index,destination_index):
                    msg = f"Card moved {str(self.tableau[source_index].peek())} ---> {str(self.foundation[destination_index].peek())} "
                    self.foundation[destination_index].push(self.tableau[source_index].pop())
                    self.count+=1
                    return msg
        
            # If the card being moved is from foundation to tableau
            if source == "F" and destination=="T":
                # If the movement is valid
                if self.valid_foundation_to_tableau_move(source_index,destination_index):
                    msg = f"Card moved {str(self.foundation[source_index].peek())} ---> {str(self.tableau[destination_index].peek())}"
                    self.tableau[destination_index].push(self.foundation[source_index].pop())
                    self.count+=1
                    return msg

            # If the card being moved is from waste to tableau
            if source == "W" and destination=="T":
                # If the movement is valid
                if self.valid_waste_to_tableau_move(destination_index):
                    msg = f"Card moved {str(self.stock_pile.peek())} ---> {str(self.tableau[destination_index].peek())}"
                    self.tableau[destination_index].push(self.stock_pile.dequeue())
                    self.count+=1
                    return msg
                    
            # If the card being moved is from waste to foundation
            if source == "W" and destination=="F":
                # If the movement is valid
                if self.valid_waste_to_foundation_move(destination_index):
                    msg = f"Card moved {str(self.stock_pile.peek())} ---> {str(self.foundation[destination_index].peek())}"
                    self.foundation[destination_index].push(self.stock_pile.dequeue())
                    self.count+=1
                    return msg
                
            # If no movement takes place returns invalid move
            return "Invalid move! "

        # If any error occurs
        except Exception as e:
            return f"Error occured: {e}"
    
    # Function to check the validity of the tableau to tableau movement
    def valid_tableau_to_tableau_move(self,source_index,destination_index):
        # If source is empty
        if self.tableau[source_index].is_empty():
            return False
        
        # Peek the cards of source and destination
        destination_card = self.tableau[destination_index].peek()
        source_card = self.tableau[source_index].peek()
        
        # If the destination tableau is empty and the source card being placed is King it is a valid move
        if (self.tableau[destination_index].is_empty() and source_card.rank=="King"):
            return True

        # If the destination is empty and source card is not a king it is not a valid move
        if (self.tableau[destination_index].is_empty() and source_card.rank!="King"):
            return False
        
        # If the source and destination both have cards then check the card's rank and color to ensure the movement
        if destination_card.check_rank_lower(source_card) and destination_card.check_card_color()!=source_card.check_card_color():
            return True
        
        # If none of the condition is valid it means the card movement is not valid
        return False
    
    # Function to check the validity of the tableau to foundation movement
    def valid_tableau_to_foundation_move(self,source_index,destination_index):
        # If source is empty
        if self.tableau[source_index].is_empty():
            return False

        # Peek the cards of source and destination
        destination_card = self.foundation[destination_index].peek()
        source_card = self.tableau[source_index].peek()

        # If the destination foundation is empty and the card being placed is Ace it is a valid move
        if (self.foundation[destination_index].is_empty() and source_card.rank=="Ace"):
            return True

        # If the destination foundation is empty and source card is not an Ace it is not a valid move
        if (self.foundation[destination_index].is_empty() and source_card.rank!="Ace"):
            return False
        
        # If the source and destination both have cards then check the source card's rank is higher and suit is same to ensure movement
        if source_card.check_rank_lower(destination_card) and destination_card.suit==source_card.suit:
            return True
        
        return False
    
    # Function to check the validity of the foundation to tableau movement
    def valid_foundation_to_tableau_move(self,source_index,destination_index):
        # If source is empty
        if self.foundation[source_index].is_empty():
            return False

        # Peek the cards of source and destination
        destination_card = self.tableau[destination_index].peek()
        source_card = self.foundation[source_index].peek()

        # If the destination tableau is empty and the card being placed is King it is a valid move
        if (self.tableau[destination_index].is_empty() and source_card.rank=="King"):
            return True

        # If the destination tableau is empty and source card is not an King it is not a valid move
        if (self.tableau[destination_index].is_empty() and source_card.rank!="King"):
            return False
        
        # If the source and destination both have cards then check the card's rank and color to ensure the movement
        if destination_card.check_rank_lower(source_card) and destination_card.check_card_color()!=source_card.check_card_color():
            return True
        
        return False 
   
    # Function to check the validity of the foundation to tableau movement
    def valid_waste_to_tableau_move(self,destination_index):
        # If source is empty
        if self.stock_pile.waste_pile.is_empty():
            return False

        # Peek the cards of source and destination
        destination_card = self.tableau[destination_index].peek()
        source_card = self.stock_pile.peek()

        # If the destination tableau is empty and the source card being placed is King it is a valid move
        if (self.tableau[destination_index].is_empty() and source_card.rank=="King"):
            return True

        # If the destination is empty and source card is not a king it is not a valid move
        if (self.tableau[destination_index].is_empty() and source_card.rank!="King"):
            return False
        
        # If the source and destination both have cards then check the card's rank and color to ensure the movement
        if destination_card.check_rank_lower(source_card) and destination_card.check_card_color()!=source_card.check_card_color():
            return True
        
        return False

    # Function to check the validity of the foundation to tableau movement
    def valid_waste_to_foundation_move(self,destination_index):
        # If source is empty
        if self.stock_pile.waste_pile.is_empty():
            return False

        # Peek the cards of source and destination
        destination_card = self.foundation[destination_index].peek()
        source_card = self.stock_pile.peek()

        # If the destination foundation is empty and the card being placed is Ace it is a valid move
        if (self.foundation[destination_index].is_empty() and source_card.rank=="Ace"):
            return True

        # If the destination is empty and source card is not an Ace it is not a valid move
        if (self.foundation[destination_index].is_empty() and source_card.rank!="Ace"):
            return False
        
        # If the source and destination both have cards then check the source card's rank is higher and suit is same to ensure movement
        if source_card.check_rank_lower(destination_card) and destination_card.suit==source_card.suit:
            return True
        
        return False
    
    # Moving multiple cards
    def move_multiple_cards(self,source_index,destination_index,card_name):
        try:
            if not game_files.utility.valid_move(source_index,destination_index):
                return "Invalid move! "
            
            print(f"{source_index}  {destination_index}")
            source_index = int(source_index)-1
            destination_index = int(destination_index)-1
            # If source is empty
            if self.tableau[source_index].is_empty():
                return "Invalid move! "
            
            # Peek the cards of source and destination
            destination_card = self.tableau[destination_index].peek()
            source_card = self.tableau[source_index].find_card(card_name)

            # If no card is found
            if source_card==None:
                return "No such card found! "
            
            # If the card is found but face down
            if source_card.face_down:
                return "No such card found! "

            # If the destination tableau is empty and the source card being placed is King it is a valid move
            if (self.tableau[destination_index].is_empty() and source_card.rank=="King"):
                self.move_cards(source_index,destination_index,card_name)
                return f"Card moved {str(source_card)} ---> {str(destination_card)}"

            # If the destination is empty and source card is not a king it is not a valid move
            if (self.tableau[destination_index].is_empty() and source_card.rank!="King"):
                return "Invalid move! "
            
            # If the source and destination both have cards then check the card's rank and color to ensure the movement
            if destination_card.check_rank_lower(source_card) and destination_card.check_card_color()!=source_card.check_card_color():
                self.move_cards(source_index,destination_index,card_name)
                return f"Card moved {str(source_card)} ---> {str(destination_card)}"
            
            # If none of the condition is valid it means the card movement is not valid
            return "Invalid move! "
        
        except Exception as e:
            return f"An error occured: {e}"

    # Moving multiple cards from source to destination
    def move_cards(self,source_index,destination_index,card_name):
        # Using a temporary stack to store the cards of the source tableau
        cards = Stack()
        while(True):
            card = self.tableau[source_index].pop()
            # Loop continues till the card is found in the source tableau
            if card.name == card_name:
                cards.push(card)
                break
            cards.push(card)

        # Pushing the cards into the destination tableau
        while not cards.is_empty():
            self.tableau[destination_index].push(cards.pop())
    
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
        
        print(f"\nMove Counts: {self.count}\n")
    
    # Drawing card from stock to waste pile
    def draw_card_from_stockpile(self):
        self.stock_pile.draw_card()
        self.count+=1
        
    # Win condition if all four foundations are filled by cards
    def game_win_condition(self):
        for foundation in self.foundation:
            if foundation.cards_count()!=13:
                return False
        return True
