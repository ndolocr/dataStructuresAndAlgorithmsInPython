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
        temp  =self.head

        while temp is not None:
            print(f"({temp.value}) -> ", end="")
            temp = temp.next
        print("None")
        return True
    
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            LinkedList.length += 1
            return new_node
        self.tail.next = new_node
        self.tail = new_node
        LinkedList.length += 1
        return new_node
    
    def pre_append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            LinkedList.length += 1
            return new_node
        new_node.next = self.head
        self.head = new_node
        LinkedList.length += 1
        return new_node
    
    def get(self, index):
        if index < 0 or index >= LinkedList.length:
            return None
        temp = self.head

        for _ in range(index):
            temp = temp.next
        return temp
    
    def pop(self):
        if self.head is None:
            self.head = None
            self.tail = None
            return None
        temp = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
            LinkedList.length -= 1
            return temp
        node = self.get(LinkedList.length - 2)
        self.tail = node
        node.next = None
        LinkedList.length -= 1
        return node
    
    def pre_pop(self):
        if self.head is None:
            self.head = None
            self.tail = None
            LinkedList.length -= 1
            return None
        temp = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
            LinkedList.length -= 1
            return temp
        head_node = self.head
        next_node = self.head.next
        head_node.next = None
        self.head = next_node
        LinkedList.length -= 1
        return head_node

    def set(self, index, value):
        node = self.get(index)

        if node is None:
            return None
        node.value = value
        return value

    def insert(self, index, value):
        if index < 0 or index >= LinkedList.length:
            return None
        if index == 0:
            return self.pre_append(value)
        if index == LinkedList.length - 1:
            return self.append(value)
        new_node = Node(value)
        temp_node = self.get(index - 1)
        new_node.next = temp_node.next
        temp_node.next = new_node
        LinkedList.length += 1
        return new_node
    
    def remove(self, index):
        node = self.get(index)
        previous_node = self.get(index - 1)

        if node is None:
            return None
        
        previous_node.next = node.next
        node.next = None
        LinkedList.length -= 1
        return node
        
    
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

    print("POP")
    my_linked_list.pop()
    my_linked_list.print_linked_list()

    print("POP")
    my_linked_list.pop()
    my_linked_list.print_linked_list()

    print("PRE-POP")
    my_linked_list.pre_pop()
    my_linked_list.print_linked_list()

    print("SET INDEX 2 TO 'WX' ")
    my_linked_list.set(2, "WX")
    my_linked_list.print_linked_list()

    print("INSERT NODE AT INDEX 0 WITH VALUE 'A' ")
    my_linked_list.insert(0, "A")
    my_linked_list.print_linked_list()

    print("INSERT NODE AT LAST INDEX WITH VALUE 'Z' ")
    my_linked_list.insert(my_linked_list.length-1, "Z")
    my_linked_list.print_linked_list()

    print("INSERT NODE AT INDEX 4 WITH VALUE 'G' ")
    my_linked_list.insert(4, "G")
    my_linked_list.print_linked_list()

    print("REMOVE NODE AT INDEX 2 ")
    my_linked_list.remove(2)
    my_linked_list.print_linked_list()



if __name__ == "__main__":
    main()

        
