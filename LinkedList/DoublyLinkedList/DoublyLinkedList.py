from DoublyLinkedList.Node import Node

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node


    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def preappend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:            
            new_node.next = self.head
            new_node.previous = None
            self.head.previous = new_node
            self.head = new_node

    def pop(self):        
        if not self.head:
            return None
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.previous

            self.tail.next = None
            temp.previous = None


    def print_linked_list(self):
        temp = self.head
        
        while temp:
            print(temp.value, end=" ⇄ ")
            temp = temp.next
        print("None")