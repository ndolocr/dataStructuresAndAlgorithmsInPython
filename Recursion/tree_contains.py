class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert_node(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root

        while(True):
            if new_node.value == temp.value:
                return False
            
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self, value):
        if self.root is None:
            return False
        
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
    def recursion_contains(self, value):
        temp = self.root
        return self.__recursion_contans(temp, value)

    def __recursion_contans(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self.__recursion_contans(current_node.left, value)
        if value > current_node.value:
            return self.__recursion_contans(current_node.right, value)
            
    
def main():
    #  Inititate Binary Search Tree
    bst = BinarySearchTree()
    print("Insert the following values:- 10 - 90")
    bst.insert_node(60)
    bst.insert_node(10)
    bst.insert_node(30)
    bst.insert_node(40)
    bst.insert_node(20)
    bst.insert_node(50)
    bst.insert_node(60)
    bst.insert_node(70)
    bst.insert_node(80)
    bst.insert_node(90)
    print(f"Confirm if 60 exists:- {bst.contains(60)}")
    print(f"Confirm if 17 exists:- {bst.contains(17)}")
    print()

    print(f"Recursion Contains")
    print("Using Recursion to check if Binary Search Tree has nodes with the following values:-")
    print(f"Confirm if 30 exists:- {bst.recursion_contains(30)}")
    print(f"Confirm if 49 exists:- {bst.recursion_contains(49)}")

if __name__ == "__main__":
    main()