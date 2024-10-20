class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push_back(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def pop_up(self):
        if self.head is None:
            print("List is empty!")
            return None
        
        if self.head.next is None:
            temp = self.head
            self.head = None
            return temp
        
        current = self.head
        while current.next.next:
            current = current.next
        temp = current.next
        current.next = None
        return temp

    def print_list(self):
        current = self.head
        if not current:
            print("List is empty!")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")