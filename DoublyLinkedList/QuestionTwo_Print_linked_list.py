class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    length = 0

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        DoublyLinkedList.length += 1

    def print_linked_list(self):
        print(f"Linked List Length:- {DoublyLinkedList.length}")

        temp = self.head

        print("None", end="")
        while temp is not None:
            print(f" <- ({temp.value}) -> ", end="")
            temp = temp.next
        print("None")

def main():
    print("INITIATE LINKED LIST")
    my_linked_list = DoublyLinkedList(5)
    my_linked_list.print_linked_list()

if __name__ == "__main__":
    main()