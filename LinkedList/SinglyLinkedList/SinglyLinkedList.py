from SinglyLinkedList.Node import Node

class SinglyLinkedList:
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
            self.tail = new_node


    def preappend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:            
            new_node.next = self.head
            self.head = new_node

    
    def print_linked_list(self):
        temp = self.head

        while temp is not None:
            print(f"{temp.value}", end=" ")
            print("→", end=" ")
            temp = temp.next
        print("None")