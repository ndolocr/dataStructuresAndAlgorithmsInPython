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
        print(f"Linked List Lenght:- {LinkedList.length}")

        temp = self.head
        while temp is not None:
            print(f"({temp.value}) -> ", end="")
            temp = temp.next
        print("None")

    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return True
        
        self.tail.next = new_node
        self.tail = new_node
        LinkedList.length += 1

        return True
    
    def per_append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return True
        
        new_node.next = self.head
        self.head = new_node
        LinkedList.length += 1

        return True
    
    def pop(self):
        
        if self.head == None:
            return None
        
        temp = self.head
        if temp == self.tail:
            self.head == None
            self.tail == None
            return temp
        
        previous = None
        current = self.head
        
        while current.next is not None:
            previous = current
            current = current.next
        
        self.tail = previous
        self.tail.next = None

        LinkedList.length -= 1
        return current
    
    def pre_pop(self):
        if self.head == None:
            return None
        
        temp = self.head
        if self.head == self.tail:
            self.head == None
            self.tail == None
            return temp
        
        current = self.head
        next_node = self.head.next

        current.next == None
        self.head = next_node
        LinkedList.length -= 1

        return current

def main():
    print("INITIATE")
    my_linked_list = LinkedList(5)    
    my_linked_list.print_linked_list()

    print("APPEND")
    my_linked_list.append(6)
    my_linked_list.append(7)
    my_linked_list.append(8)
    my_linked_list.print_linked_list()

    print("PRE-APPEND")
    my_linked_list.per_append(4)
    my_linked_list.per_append(3)
    my_linked_list.per_append(2)
    my_linked_list.per_append(1)
    my_linked_list.print_linked_list()

    print("POP (3 Node)")
    my_linked_list.pop()
    my_linked_list.pop()
    my_linked_list.pop()
    my_linked_list.print_linked_list()

    print("PRE-POP (2 Nodes)")
    my_linked_list.pre_pop()
    my_linked_list.pre_pop()
    my_linked_list.print_linked_list()

if __name__ == "__main__":
    main()