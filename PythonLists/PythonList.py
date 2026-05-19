class PythonListClass:
    """
        Python Lists
        This Class is used to create the List data structure.
        All possible actions for the list will be covered as well as their Time Complexity
        1. Append - O(1)
    """
    length = 0

    def __init__(self, value):
        self.my_list = [value]
    
    def list_append(self, value):
        """
        """
        return self.my_list.append(value)
    
    def list_insert(self, index, value):
        return self.my_list.insert(index, value)
    
    def list_extend(self, list_items):
        return self.my_list.extend(list_items)
    
    def print_full_list(self):
        print(self.my_list)