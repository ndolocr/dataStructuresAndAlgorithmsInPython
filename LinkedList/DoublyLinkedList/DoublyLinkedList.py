from DoublyLinkedList.Node import Node

class DoublyLinkedList:
    length = 0
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        DoublyLinkedList.length += 1


    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        DoublyLinkedList.length += 1

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
        DoublyLinkedList.length += 1

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
        DoublyLinkedList.length -= 1


    def get_node_by_index(self, index):
        temp = self.head
        if index < 0 or index > DoublyLinkedList.length:
            print("Invalid index used to get a node")
            return None
        for _ in range(index):
            temp = temp.next
        print(f"The Value at index {index} is {temp.value}")
        return temp
    

    def change_node_value_by_index(self, index, value):
        temp = self.head
        if index < 0 or index > DoublyLinkedList.length:
            print("Invalid index used to get a node")
            return None
        for _ in range(index):
            temp = temp.next
        old_value = temp.value
        temp.value = value
        print(f"The current value at index {index} is {old_value}, the updated value is {temp.value}")


    def print_linked_list(self):
        temp = self.head
        
        while temp:
            print(temp.value, end=" ⇄ ")
            temp = temp.next
        print("None")