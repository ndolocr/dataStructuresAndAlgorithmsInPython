from SinglyLinkedList.Node import Node

class SinglyLinkedList:
    length = 0
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        SinglyLinkedList.length += 1


    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        SinglyLinkedList.length += 1


    def preappend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:            
            new_node.next = self.head
            self.head = new_node
        SinglyLinkedList.length += 1

    def pop(self):
        temp = self.head
        pre = None

        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        pre.next = None

        SinglyLinkedList.length -= 1
        
    def get_by_index(self, index):
        temp = self.head
        if index < 0 or index > SinglyLinkedList.length:
            print("Invalid index used to get a node")
            return None
        for _ in range(index):
            temp = temp.next
        print(f"The Value at index {index} is {temp.value}")
        return temp
    
    def change_node_value_by_index(self, index, value):
        temp = self.head
        if index < 0 or index > SinglyLinkedList.length:
            c
            return
        for _ in range(index):
            temp = temp.next
        old_value = temp.value
        temp.value = value
        print(f"The current value at index {index} is {old_value}, the updated value is {temp.value}")
    
    def insert_value(self, index, value):
        prev = None
        temp = self.head

        if index < 0 or index > SinglyLinkedList.length:
            print("Invalid index used to get a node")
            return None
        # Previous to point to current node.
        for _ in range(index):
            prev = temp
            temp = temp.next
        new_node = Node(value)
        prev.next = new_node
        new_node.next = temp


    def remove_node(self, index):
        if index <0 or index > SinglyLinkedList.length:
            print("Invalid index used to get a node")
            return None
        prev = None
        temp = self.head

        for _ in range(index):
            prev = temp
            temp = temp.next
        prev.next = temp.next
        temp.next = None
        
    def print_linked_list(self):
        temp = self.head

        while temp is not None:
            print(f"{temp.value}", end=" ")
            print("→", end=" ")
            temp = temp.next
        print("None")