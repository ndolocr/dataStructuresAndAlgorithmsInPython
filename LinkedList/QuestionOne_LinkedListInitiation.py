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

        while temp is not None:
            print(f"({temp.value}) -> ", end=" ")
            temp = temp.next
        print("None")

def main():
    linked_list = LinkedList(2)
    linked_list.print_linked_list()

if __name__ == "__main__":
    main()