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
            if self.first == temp and self.last == temp:
                print("FIRST")
                print("  |")
                print("  v")
                print(f" ({temp.value}) -> None")
                print("  |")
                print("  v")
                print("LAST")
            elif self.first == temp:
                print("FIRST")
                print("  |")
                print("  v")
                print(f" ({temp.value}) -> ", end="")

            elif self.last == temp:
                print(f" ({temp.value}) -> None")
                print("  |")
                print("  v")
                print("LAST")            
            
            else:
                print(f"({temp.value}) -> ", end="")
            temp = temp.next

def main():
    print("QUEUE INITIATION")
    my_queue = Queue(1)
    my_queue.print_queue()

if __name__ == "__main__":
    main()