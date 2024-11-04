import os
import sys
from linked_list import LinkedList,Node

# # setting paths
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from BL.card_bl import Card

class Stack:
    # initalizing the stack
    def __init__(self):
        self.linkedList = LinkedList()
    
    # pushing back the card into the stack
    def push(self,card):
        node = Node(card)
        self.linkedList.insertAtTail(node)
    
    # poping the card from the stack
    def pop(self):
        return self.linkedList.deleteFromTail()