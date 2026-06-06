from Node import Node

class LinkedList:
    lenght = 0

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        LinkedList.lenght = 1

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        elif self.head == self.tail:
            self.head.next = new_node
            self.tail = new_node            
        else:
            temp = self.tail
            temp.next = new_node
            self.tail = new_node
        LinkedList.lenght += 1

    def pre_append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        LinkedList.lenght += 1

    def pop(self):
        if self.head == None:
           self.head = None
           self.tail = None
           LinkedList.lenght = 0
        elif self.head == self.tail:
           self.head = None
           self.tail = None
           LinkedList.lenght -= 1
        else:
            current = self.head
            previous_node = None

            while current is not None:
                previous_node = current
                current = current.next
            self.tail = previous_node
            previous_node.next = None

            LinkedList.lenght -= 1
    
    def front_pop(self):
        if self.head is None:
            self.head = None
            self.tail = None
            LinkedList.lenght = 0

        elif self.head == self.tail:
            self.head = None
            self.tail = None
            LinkedList.lenght -= 1
        
        else:
            second_node = self.head.next
            self.head.next = None
            self.head = second_node
            LinkedList.lenght -= 1

    def insert_before_value(self, value, before_node_value):
        if self.head is None:
            self.head = None
            self.tail = None
            return None
        if self.head == self.tail:
            if self.head.value == value:
                new_node = Node(value)
                new_node.next = self.head
                self.head = new_node
        else:
            new_node = Node(value)
            if self.head.value == value:                
                new_node.next = self.head
                self.head = new_node
            else:
                previous_node = None
                current_node = self.head

                while current_node is not None:
                    if current_node.value == before_node_value:
                        previous_node.next = new_node
                        new_node.next = current_node
                    previous_node = current_node
                    current_node = current_node.next
    
    def insert_after_value(self):
        pass
    
    def print_linked_list(self):        
        temp = self.head

        while temp:
            print(f"{temp.value}", end=" -> ")
            temp = temp.next