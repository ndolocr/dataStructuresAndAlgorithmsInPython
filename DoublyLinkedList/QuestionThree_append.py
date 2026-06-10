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
        print(f"Linked List Length:- {DoublyLinkedList.length}")

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
        return new_node

def main():
    print("Doubly Linked List Initiation")
    my_doubly_linked_list = DoublyLinkedList(6)
    my_doubly_linked_list.print_doubly_linked_list()

    print()
    print("Append value 7")
    my_doubly_linked_list.append(7)
    my_doubly_linked_list.print_doubly_linked_list()

    print()
    print("Append value 8")
    my_doubly_linked_list.append(8)
    my_doubly_linked_list.print_doubly_linked_list()

if __name__ == "__main__":
    main()