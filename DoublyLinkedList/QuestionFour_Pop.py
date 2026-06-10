class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    length = 0

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        DoublyLinkedList.length += 1

    def print_doubly_linked_list(self):
        print(f"Doubly Linked List Length :- {DoublyLinkedList.length}")

        temp = self.head
        print("None", end="")
        while temp is not None:
            print(f" <- ({temp.value}) -> ", end="")
            temp = temp.next
        print("None")
        return True
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            DoublyLinkedList.length += 1
            return new_node
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        DoublyLinkedList.length += 1
        return new_node
    
    def pop(self):
        if self.head is None:
            return None
        temp = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
            DoublyLinkedList.length -= 1
            return temp
        
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        DoublyLinkedList.length -= 1
        return temp

    
    def pop_old(self):
        if self.head is None:
            return None
        temp = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
            DoublyLinkedList.length -= 1
            return temp
        
        previous_node = None
        current_node = self.head

        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next
        current_node.prev = None
        previous_node.next = None
        self.tail = previous_node
        DoublyLinkedList.length -= 1
        return current_node

def main():
    print()
    print("DOUBLY LINKED LIST INITIATION")
    my_doubly_linked_list = DoublyLinkedList(5)
    my_doubly_linked_list.print_doubly_linked_list()

    print()
    print("APPEND NODE 6")
    my_doubly_linked_list.append(6)
    my_doubly_linked_list.print_doubly_linked_list()

    print()
    print("APPEND NODE 7")
    my_doubly_linked_list.append(7)
    my_doubly_linked_list.print_doubly_linked_list()

    print()
    print("POP NODE")
    my_doubly_linked_list.pop()
    my_doubly_linked_list.print_doubly_linked_list()

    print()
    print("POP NODE")
    my_doubly_linked_list.pop()
    my_doubly_linked_list.print_doubly_linked_list()

if __name__ == "__main__":
    main()