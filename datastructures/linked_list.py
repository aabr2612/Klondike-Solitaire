import sys
import os

# setting paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from BL.card_bl import Card

# node class
class Node:
    # initializing node
    def __init__(self, card):
        self.card = Card(card.rank,card.suit)
        self.next = None

# linkedlist
class LinkedList:
    # initalizing linkedlist
    def __init__(self):
        self.head = None
    
    # insertion of cards at tail
    def insertAtTail(self, card):
        new_node = Node(card) # new node to be added
        
        # head is empty
        if self.head is None:
            self.head = new_node
        # inserting at the end
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    # removing card from tail
    def deleteFromTail(self):
        # if the list is not empty
        if self.head is not None:
            # if the head next is empty
            if self.head.next is None:
                temp = self.head
                self.head = None
                return temp
            # keeps traversing till last element found
            else:
                current = self.head
                while current.next.next is not None:
                    current = current.next
                temp = current.next
                current.next = None
                return temp
        # if head empty it means list is empty
        else:
            print("No cards!")
            return None
    
    # function to remove a number of cards at a time from a linkedlist
    def removingCardsFromPosition(self,card):
        if self.head == None:
            print ("Empty! No card to move!")
        else:
            current = self.head
            while current and current.card.rank!=card.rank and current.card.suit!=card.suit:
                current = current.next
            if current:
                return current
            else:
                print("No such card found!") 
                return None
    
    # function to display the cards at a time
    def display(self):
        current = self.head
        if current is None:
            print("List is empty!")
            return
        while current is not None:
            print(current.card.rank, end=" -> ")
            current = current.next
        print("None")