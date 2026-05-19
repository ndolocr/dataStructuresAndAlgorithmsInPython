from DoublyLinkedList.Node import Node

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(5)
        self.head = new_node
        self.tail = new_node

    def print_linked_list(self):
        temp = self.head
        
        # print("None", end="→")
        while temp:
            if temp is self.tail:
                print(f"None ← ({temp.value}) → None")
            else:
                print("None ", end=" ← ")
                if temp.next is None:
                    print(f"({temp.value})", end=" → ")
                else:
                    print(f"({temp.value})", end=" ⇄ ")
            temp = temp.next