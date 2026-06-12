class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return new_node
        
        temp = self.root

        while(True):
            if temp.value == new_node.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return new_node
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return new_node
                temp = temp.right

def main():
    print("INITITATE BINARY SEARCH TREE")
    my_tree = BinarySearchTree()
    my_tree.print_tree()

    print("INSERT NEW NODE 5")
    my_tree.insert(5)
    my_tree.print_tree()

    print("INSERT NEW NODE 4")
    my_tree.insert(4)
    my_tree.print_tree()

    print("INSERT NEW NODE 8")
    my_tree.insert(8)
    my_tree.print_tree()

if __name__ == "__main__":
    main()