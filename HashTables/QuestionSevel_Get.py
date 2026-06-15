class HashTable:
    def __init__(self, size  = 7):
        self.list_item = [None] * size

    def print_hash_table(self):
        for key, value in enumerate(self.list_item):
            print(f"{key} : {value}")

        return self.list_item
    
    def calculate_hash_index(self, key):
        hashed_index = 0
        for letter in key:
            hashed_index = (hashed_index + ord(letter) * 23) % len(self.list_item)
        return hashed_index
    
    def set_value(self, key, value):
        index = self.calculate_hash_index(key)
        if self.list_item[index] is None:
            self.list_item[index] = []
        self.list_item[index].append([key, value])

        return [key, value]
    
    def get_value(self, key):
        index = self.calculate_hash_index(key)
        print(f"Index --> {index}")
        if self.list_item[index] is not None:
            for i in range(len(self.list_item[index])):
                if self.list_item[index][i][0] == key:
                    return self.list_item[index][i][1]
        return None
    
def main():
    # Initiate Hash Table
    hash_table = HashTable()

    print(f"Hash Table:- ")
    hash_table.print_hash_table()

    print()
    key = "Bolts"
    print(f"Value -> {key}")
    print(f"Calculated index from --> {key} is:- {hash_table.calculate_hash_index(key)}")
    hash_table.set_value(key, "1000")
    print(f"Hash Table:- ")
    hash_table.print_hash_table()

    print()
    key = "Nails"
    print(f"Value -> {key}")
    print(f"Calculated index from --> {key} is:- {hash_table.calculate_hash_index(key)}")
    hash_table.set_value(key, "2000")
    print(f"Hash Table:- ")
    hash_table.print_hash_table()

    print()
    key = "Saw"
    print(f"Value -> {key}")
    print(f"Calculated index from --> {key} is:- {hash_table.calculate_hash_index(key)}")
    hash_table.set_value(key, "3000")
    print(f"Hash Table:- ")
    hash_table.print_hash_table()

    print()
    key = "Hammers"
    print(f"Value -> {key}")
    print(f"Calculated index from --> {key} is:- {hash_table.calculate_hash_index(key)}")
    hash_table.set_value(key, "2000")
    print(f"Hash Table:- ")
    hash_table.print_hash_table()

    print()
    key = "Hammers"
    print(f"Value -> {key}")
    print(f"Get Value at key of --> {key}")
    print(f"Value got is:- {hash_table.get_value(key)}")

    print()
    key = "Saw"
    print(f"Value -> {key}")
    print(f"Get Value at key of --> {key}")
    print(f"Value got is:- {hash_table.get_value(key)}")
    

if __name__ == "__main__":
    main()