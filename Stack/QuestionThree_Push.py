class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def print_stack(self):
        print(f"Stack Length:- {self.length}")
        
        temp = self.top
        while temp is not None:
            print(f"{temp.value}")
            print("|")
            print("v")
            temp = temp.next
        print("None")
        return True
    
    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node            
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
        return new_node
    
def main():
    print("STACK INITIATION")
    my_stack = Stack(9)
    my_stack.print_stack()

    print()
    print("PUSH VALUE 8 to STACK")
    my_stack.push(8)
    my_stack.print_stack()

    print()
    print("PUSH VALUE 7 to STACK")
    my_stack.push(7)
    my_stack.print_stack()

if __name__ == "__main__":
    main()