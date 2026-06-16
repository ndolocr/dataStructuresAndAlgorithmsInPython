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
        
        temp = self.root
        while(True):
            if temp.value == value:
                return False
            if value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            if value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            if value == temp.value:
                return False
            
    def recursion_insert(self, value):
        return self.__recursion_insert(self.root, value)
    
    def __recursion_insert(self, current_node, value):
        if current_node is None:
            current_node = Node(value)
            return current_node
        
        if value < current_node.value:
            current_node.left = self.__recursion_insert(current_node.left, value)
    
        if value > current_node.value:
            current_node.right = self.__recursion_insert(current_node.right, value)
        
        return current_node
        

    
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
        return self.__recursion_contains(self.root, value)
    
    def __recursion_contains(self, current_node, value):
        if current_node is None:
            return False
        
        while current_node is not None:
            if value < current_node.value:
                return self.__recursion_contains(current_node.left, value)
            elif value > current_node.value:
                return self.__recursion_contains(current_node.right, value)
            else:
                return True
        return False

def main():
    # Initiate Binary Search Tree
    bst = BinarySearchTree()

    # Insert Nodes
    print("Insert Nodes 10 and 60 using while loop")
    bst.insert(60)
    bst.insert(10)
    print()
    print("Insert Nodes 20 and 50 using Recursion")
    bst.recursion_insert(20)
    bst.recursion_insert(30)
    bst.recursion_insert(40)
    bst.recursion_insert(50)
    print()
    print("Check if Tree contaisn the following values (using while loop)")
    print(f"Confirm if 60 exists:- {bst.contains(60)}")
    print(f"Confirm if 71 exists:- {bst.contains(71)}")
    print()
    print("Check if Tree contaisn the following values (using Recursion)")
    print(f"Confirm if 50 exists:- {bst.recursion_contains(50)}")
    print(f"Confirm if 11 exists:- {bst.recursion_contains(11)}")
    print(f"Confirm if 20 exists:- {bst.recursion_contains(20)}")
    print(f"Confirm if 13 exists:- {bst.recursion_contains(13)}")

if __name__ == "__main__":
    main()