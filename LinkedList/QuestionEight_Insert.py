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
        return True
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            LinkedList.length += 1
            return True
        self.tail.next = new_node
        self.tail = new_node
        LinkedList.length += 1
        return True
    
    def pre_append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            LinkedList.length += 1
            return True
        new_node.next = self.head
        self.head = new_node
        LinkedList.length += 1
        return True
    
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
        
        previous_node = None
        current_node =  self.head
        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        self.tail = previous_node
        LinkedList.length -= 1
        return current_node
    
    def pre_pop(self):
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
        current_node = self.head
        next_node = self.head.next

        current_node.next = None
        self.head = next_node
        LinkedList.length -= 1
        return current_node
    
    def get_for(self, index):
        if index < 0 or index >= LinkedList.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def get_while(self, index):
        if index < 0 or index >= LinkedList.length:
            return None
        
        num = 0
        temp = self.head
        while num < index:
            temp = temp.next
            num += 1
        return temp
    
    def set(self, index, value):
        node = self.get_for(index)

        if node is not None:
            node.value = value
            return node
        return None
    
    def insert(self, index, value):
        if index < 0 or index >= LinkedList.length:
            return False
        
        if index == 0:
            return self.pre_append(value)
        
        if index == LinkedList.length - 1:
            return self.append(value)
        
        new_node = Node(value)
        pre_node = self.get_while(index - 1)
        new_node.next = pre_node.next
        pre_node.next = new_node
        LinkedList.length += 1
        return True
            
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
    while_get = my_linked_list.get_while(1)
    print(f"GOT VALUE --> {while_get.value}")

    print("FOR LOOP GET")
    for_get = my_linked_list.get_for(2)
    print(f"GOT VALUE --> {for_get.value}")

    print("SET VALUE AT INDEX 1 to 15")
    my_linked_list.set(1, "G")
    my_linked_list.print_linked_list()

    print("INSERT NODE WITH VALUE X in index 4")
    my_linked_list.insert(4, "X")
    my_linked_list.print_linked_list()

if __name__ == "__main__":
    main()