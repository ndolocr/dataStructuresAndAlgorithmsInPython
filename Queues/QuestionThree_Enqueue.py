class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        print(f"Queue Length:- {self.length}")
        temp = self.first

        while temp is not None:
            print(f"({temp.value}) -> ", end="")
            temp = temp.next
        print("None")
        return True
    
    def enqueue(self, value):
        new_node = Node(value)

        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return new_node

def main():
    print("QUEUE INITIATION")
    my_queue = Queue(1)
    my_queue.print_queue()

    print()
    print("ENQUEUE VALUE 2")
    my_queue.enqueue(2)
    my_queue.print_queue()

    print()
    print("ENQUEUE VALUE 3")
    my_queue.enqueue(3)
    my_queue.print_queue()

    print()
    print("ENQUEUE VALUE 4")
    my_queue.enqueue(4)
    my_queue.print_queue()

    print()
    print("ENQUEUE VALUE 5")
    my_queue.enqueue(5)
    my_queue.print_queue()

if __name__ == "__main__":
    main()