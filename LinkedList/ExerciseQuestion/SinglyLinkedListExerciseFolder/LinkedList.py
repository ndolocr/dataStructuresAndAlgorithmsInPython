from SinglyLinkedListExerciseFolder.Node import Node

class LinkedList:
    length = 0
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        LinkedList.length += 1
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def print_linked_list(self):
        temp = self.head

        while temp is not None:
            print(f"({temp.value})", end=" --> ")
            temp = temp.next
        print("None")
    
    # QUESTIONS
    def get_middle_node(self):
        """
        Instructions:
        Write a method to find and return the middle node in the Linked List WITHOUT using the length attribute.
        """

        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        print(f"Middle Node is  --> {slow_pointer.value}")