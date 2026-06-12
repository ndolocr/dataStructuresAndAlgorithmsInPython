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
        temp = self.top

        while temp is not None:
            print(f"({temp.value})")
            print(" |")
            print(" v")
            temp = temp.next
        print("None")
        return True
    
def main():
    print("STACK INITIALIZATION")
    my_stack = Stack(9)
    my_stack.print_stack()

if __name__ == "__main__":
    main()