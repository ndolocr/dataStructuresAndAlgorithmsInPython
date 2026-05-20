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
    
    def print_linked_list(self):
        temp = self.head

        while temp is not None:
            print(f"{temp.value}", end=" ")
            print("→", end=" ")
            temp = temp.next
        print("None")