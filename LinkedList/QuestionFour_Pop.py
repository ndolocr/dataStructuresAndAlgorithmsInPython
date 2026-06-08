class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    lenght = 0

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        LinkedList.lenght += 1

    def print_linked_list(self):
        print(f"Linked List Length:- {LinkedList.lenght}")
        temp = self.head

        print("Linked List:- ", end="")
        while temp is not None:
            print(f"({temp.value}) -> ", end="")
            temp = temp.next
        print(None)

    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        LinkedList.lenght += 1

        return True
    
    def pre_append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        LinkedList.lenght += 1

        return True
    
    def pop(self):
        if self.head == None:
            return None
        temp = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return temp
        
        previous = None
        current = self.head

        while current.next is not None:
            previous = current
            current = current.next
        self.tail = previous
        self.tail.next = None
        LinkedList.lenght -= 1

        return current
    
def main():
    print()
    print("INITIAL")
    my_linked_list = LinkedList(6)
    my_linked_list.print_linked_list()
    
    print()
    print("APPEND")
    my_linked_list.append(7)
    my_linked_list.append(8)
    my_linked_list.append(9)

    my_linked_list.print_linked_list()

    print()
    print("PRE-APPEND")
    my_linked_list.pre_append(5)
    my_linked_list.pre_append(4)

    my_linked_list.print_linked_list()

    print()
    print("POP")
    my_linked_list.pop()
    my_linked_list.print_linked_list()

    print()
    print("POP")
    my_linked_list.pop()
    my_linked_list.print_linked_list()

if __name__ == "__main__":
    main()