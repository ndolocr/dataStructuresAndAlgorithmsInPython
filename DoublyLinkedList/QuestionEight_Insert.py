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
        print("None", end="")
        temp = self.head
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
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        DoublyLinkedList.length += 1
        return new_node
    
    def pre_append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        DoublyLinkedList.length += 1
        return new_node
    
    def get(self, index):
        if index < 0 or index >= DoublyLinkedList.length:
            return None
        if index < DoublyLinkedList.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            temp = self.tail
            for _ in range(DoublyLinkedList.length - 1, index, -1):
                temp = temp.prev
            return temp
    
    def set(self, index, value):
        node = self.get(index)

        if node is None:
            return None
        node.value = value
        return node
    
    def insert(self, index, value):
        new_node = Node(value)
        
        before_node = self.get(index - 1)
        after_node = before_node.next

        new_node.next = after_node
        new_node.prev = before_node

        after_node.prev = new_node
        before_node.next = new_node
        return new_node
    
def main():
    print("INITIATING DOUBLY LINKED LIST")
    my_doubly_linked_list = DoublyLinkedList(5)
    my_doubly_linked_list.print_doubly_linked_list()

    print("APPEND:- 6")
    my_doubly_linked_list.append(6)
    my_doubly_linked_list.print_doubly_linked_list()

    print("APPEND:- 7")
    my_doubly_linked_list.append(7)
    my_doubly_linked_list.print_doubly_linked_list()

    print("APPEND:- 8")
    my_doubly_linked_list.append(8)
    my_doubly_linked_list.print_doubly_linked_list()

    print("PRE-APPEND:- 4")
    my_doubly_linked_list.pre_append(4)
    my_doubly_linked_list.print_doubly_linked_list()

    print("PRE-APPEND:- 3")
    my_doubly_linked_list.pre_append(3)
    my_doubly_linked_list.print_doubly_linked_list()

    print("PRE-APPEND:- 2")
    my_doubly_linked_list.pre_append(2)
    my_doubly_linked_list.print_doubly_linked_list()

    print("PRE-APPEND:- 1")
    my_doubly_linked_list.pre_append(1)
    my_doubly_linked_list.print_doubly_linked_list()

    print("GET AT INDEX:- 4")
    my_doubly_linked_list.get(4)
    my_doubly_linked_list.print_doubly_linked_list()

    print("SET X AT INDEX:- 3")
    my_doubly_linked_list.set(3, "X")
    my_doubly_linked_list.print_doubly_linked_list()

    print("INSERT Y AT INDEX:- 4")
    my_doubly_linked_list.insert(4, "Y")
    my_doubly_linked_list.print_doubly_linked_list()


if __name__ == "__main__":
    main()
        

