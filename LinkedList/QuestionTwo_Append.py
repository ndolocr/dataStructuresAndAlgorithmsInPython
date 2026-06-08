class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LiknedList:
    length = 0
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        LiknedList.length += 1
    
    def print_linked_list(self):
        temp = self.head
        print(f"Linked List Length --: {LiknedList.length}")
        while temp is not None:
            print(f"({temp.value}) -> ", end="")
            temp = temp.next
        print("None")
    
    def append(self, value):
        # Check to see if Linked List is Empty
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        LiknedList.length += 1
    
def main():
    my_linked_list = LiknedList(0)
    my_linked_list.append(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.append(5)

    my_linked_list.print_linked_list()

if __name__ == "__main__":
    main()