class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    length = 0
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        LinkedList.length += 1

    def print_linked_list(self):
        temp = self.head

        print(f"Linked List Length --: {LinkedList.length}")
        print("Linked List:- ", end=" ")
        while temp is not None:
            print(f"({temp.value}) -> ", end="")
            temp = temp.next
        print("None")

    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        LinkedList.length += 1
        return True
    
    def pre_append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        LinkedList.length += 1
        return True

def main():
    my_linked_list = LinkedList(4)

    my_linked_list.append(5)
    my_linked_list.append(6)
    my_linked_list.append(7)
    my_linked_list.append(8)
    my_linked_list.append(9)

    my_linked_list.pre_append(3)
    my_linked_list.pre_append(2)
    my_linked_list.pre_append(1)

    my_linked_list.print_linked_list()

if __name__ == "__main__":
    main()