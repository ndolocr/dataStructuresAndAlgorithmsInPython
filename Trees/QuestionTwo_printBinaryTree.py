class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def print_tree(self):
        temp = self.root

        while temp is not None:
            print(f"({temp.value})")
        print("None")
        return True

def main():
    print("INITITATE BINARY SEARCH TREE")
    my_tree = BinarySearchTree()
    my_tree.print_tree()

if __name__ == "__main__":
    main()