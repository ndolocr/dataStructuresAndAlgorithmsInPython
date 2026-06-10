class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None

class DoublyLinkedList:
    length = 0
    
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        DoublyLinkedList.length += 1