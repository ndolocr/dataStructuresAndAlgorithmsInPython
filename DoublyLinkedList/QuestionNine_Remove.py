class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_doubly_linked_list(self):
        print(f"LINKED LIST Lenght:- {self.length}")

        temp = self.head
        print("None")
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
        self.length += 1
        return new_node
    
    def pre_append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return new_node
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        if index < self.length/2:
            num = 0
            while num < index:
                temp = temp.next
                num += 1
            return temp
        else:
            temp = self.tail
            num = self.length - 1
            while num > index:
                temp = temp.prev
                num -= 1
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
        next_node = before_node.next

        before_node.next = new_node
        new_node.next = next_node

        next_node.prev = new_node
        new_node.prev = before_node
        self.length += 1

        return new_node
    
    def remove(self, index):
        node = self.get(index)
        before_node = node.prev
        next_node = node.next

        before_node.next = next_node
        next_node.prev = before_node

        node.next = None
        node.prev = None
        self.length -= 1

        return node
    
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

    print("REMOVE NODE AT INDEX:- 4")
    my_doubly_linked_list.remove(4)
    my_doubly_linked_list.print_doubly_linked_list()


if __name__ == "__main__":
    main()
        

