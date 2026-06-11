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
        print(f"Doubly Linked List Length:- {DoublyLinkedList.length}")
        temp = self.head

        print("None", end="")
        while temp is not None:
            print(f" <- ({temp.value}) -> ", end="")
            temp = temp.next
        print("None")

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return new_node
        self.tail.next = new_node
        new_node.prev = None
        self.tail = new_node
        return new_node
    
    def pre_append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            DoublyLinkedList.length += 1
            return new_node        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        DoublyLinkedList.length += 1
        return new_node
    
    def pop(self):
        if self.head is None:
            self.head = None
            self.tail = None
            return None
        if self.head == self.tail:
            self.head = None
            self.tail = None
            DoublyLinkedList.length -= 1
            return None
        temp = self.tail
        before = self.tail.prev
        print(f"BEFORE NODE:- {before}")
        before.next = None
        temp.prev = None
        self.tail = before
        DoublyLinkedList.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= DoublyLinkedList.length:
            return None
        temp = self.head
        if index < DoublyLinkedList.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(DoublyLinkedList.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def set(self, index, value):
        node = self.get(index)

        if not node:
            return None
        node.value = value
        return node

def main():
    print("DOUBLY LINKED LIST INITIATION")
    my_doubly_linked_list = DoublyLinkedList(5)
    my_doubly_linked_list.print_doubly_linked_list()

    print()
    print("APPEND 6")
    my_doubly_linked_list.append(6)
    my_doubly_linked_list.print_doubly_linked_list()

    print()
    print("APPEND 7")
    my_doubly_linked_list.append(7)
    my_doubly_linked_list.print_doubly_linked_list()

    print()
    print("PRE-APPEND 4")
    my_doubly_linked_list.pre_append(4)
    my_doubly_linked_list.print_doubly_linked_list()

    print()
    print("PRE-APPEND 3")
    my_doubly_linked_list.pre_append(3)
    my_doubly_linked_list.print_doubly_linked_list()

    print()
    print("PRE-APPEND 2")
    my_doubly_linked_list.pre_append(2)
    my_doubly_linked_list.print_doubly_linked_list()

    print()
    print("PRE-APPEND 1")
    my_doubly_linked_list.pre_append(1)
    my_doubly_linked_list.print_doubly_linked_list()

    # print()
    # print("POP")
    # my_doubly_linked_list.pop()
    # my_doubly_linked_list.print_doubly_linked_list()

    # print()
    # print("POP")
    # my_doubly_linked_list.pop()
    # my_doubly_linked_list.print_doubly_linked_list()

    print()
    print("GET NODE AT INDEX 2:- ", end="")
    print(my_doubly_linked_list.get(2).value)
    
    print()
    print("SET INDEX 2 TO VALUE 'X' ")
    my_doubly_linked_list.set(2, "X")
    my_doubly_linked_list.print_doubly_linked_list()

if __name__ == "__main__":
    main()