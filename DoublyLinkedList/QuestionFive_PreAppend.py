class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    length = 0

    def __init__(self, value):
        new_node = Node(value)
        self.head = None
        self.tail = None
        DoublyLinkedList.length += 1

    def print_linked_list(self):
        print(f"Doubly Linked List Length:- {DoublyLinkedList.length}")

        temp = self.head
        print("None")
        while temp is not None:
            print(f" <- ({temp.value}) -> ", end="")
            temp = temp.next
        print("None")

        return None
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return new_node
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        return new_node
    
    def pre_append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = None
            self.tail = None
            DoublyLinkedList.length += 1
            return new_node
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
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
        
        temp_tail = self.tail
        self.tail = temp_tail.prev
        self.tail.next = None
        temp_tail.prev = None
        DoublyLinkedList.length -= 1
        return temp_tail
    
def main():
    print("INITIATING DOUBLY LINKED LIST")
    my_doubly_linked_list = DoublyLinkedList(5)
    my_doubly_linked_list.print_linked_list()

    print()
    print("APPEND 6")
    my_doubly_linked_list.append(6)
    my_doubly_linked_list.print_linked_list()

    print()
    print("APPEND 6")
    my_doubly_linked_list.append(7)
    my_doubly_linked_list.print_linked_list()

    print()
    print("PRE-APPEND 4")
    my_doubly_linked_list.pre_append(4)
    my_doubly_linked_list.print_linked_list()

    print()
    print("PRE-APPEND 3")
    my_doubly_linked_list.pre_append(3)
    my_doubly_linked_list.print_linked_list()

    print()
    print("POP")
    my_doubly_linked_list.pop()
    my_doubly_linked_list.print_linked_list()

    print()
    print("POP")
    my_doubly_linked_list.pop()
    my_doubly_linked_list.print_linked_list()

if __name__ == "__main__":
    main()