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
        print(f"Linked List Length:- {LinkedList.length}")

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
    
    def pre_append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail =  new_node
            return True
        new_node.next = self.head
        self.head = new_node
        LinkedList.length += 1
        return True
    
    def pop(self):
        if self.head == None:
            return None
        temp = self.head
        if self.head == self.tail:
            self.head == None
            self.tail == None
            LinkedList.length -= 1
            return temp
        
        previous = None
        current = self.head
        while current.next is not None:
            previous = current
            current = current.next
        
        self.tail = previous
        self.tail.next = None
        return current
    
    def pre_pop(self):
        if self.head == None:
            return None
        current = self.head
        next_node = self.head.next

        self.head = next_node
        current.next = None
        LinkedList.length -= 1
        return current

    def get(self, index):
        if index < 0 or index >=LinkedList.length:
            return None
        
        num = 0
        temp = self.head
        while num < index:
            temp = temp.next
            num += 1
        return temp
    
    def get_for(self, index):
        if index < 0 or index >= LinkedList.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
def main():
    print("INITIALIZE")
    my_linked_list = LinkedList(5)
    my_linked_list.print_linked_list()

    print("APPEND")
    my_linked_list.append(6)
    my_linked_list.append(7)
    my_linked_list.append(8)
    my_linked_list.append(9)
    my_linked_list.print_linked_list()

    print("PRE-APPEND")
    my_linked_list.pre_append(4)
    my_linked_list.pre_append(3)
    my_linked_list.pre_append(2)
    my_linked_list.pre_append(1)
    my_linked_list.print_linked_list()

    print("POP")
    my_linked_list.pop()
    my_linked_list.print_linked_list()

    print("PRE-POP")
    my_linked_list.pre_pop()
    my_linked_list.print_linked_list()

    print("WHILE LOOP GET")
    while_get = my_linked_list.get(1)
    print(f"GOT VALUE --> {while_get.value}")

    print("FOR LOOP GET")
    for_get = my_linked_list.get_for(2)
    print(f"GOT VALUE --> {for_get.value}")

if __name__ == "__main__":
    main()