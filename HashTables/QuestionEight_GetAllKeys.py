class HashTable:
    def __init__(self, size = 7):
        self.list_items = [None] * size

    def print_hash_table(self):
        for key, value in enumerate(self.list_items):
            print(f"{key} : {value}")
        return self.list_items
    
    def calculate_index(self, key):
        hashed_value = 0
        for letter in key:
            hashed_value = (hashed_value + ord(letter) * 23) % len(self.list_items)
        return hashed_value
    
    def set_value(self, key, value):
        index = self.calculate_index(key)

        if self.list_items[index] is None:
            self.list_items[index] = []
        self.list_items[index].append([key, value])

        return [key, value]
    
    def get_value(self, key):
        index = self.calculate_index(key)

        if self.list_items[index] is not None:
            for i in range(len(self.list_items[index])):
                if self.list_items[index][i][0] == key:
                    return self.list_items[index][i][1]
        return None
    
    def get_all_keys(self):
        all_keys = []
        for col in range(len(self.list_items)):
            if self.list_items[col] is not None:
                for i in range(len(self.list_items[col])):
                    all_keys.append(self.list_items[col][i][0])
        return all_keys 

def main():
    # Initiate Hash Table
    hash_table = HashTable()

    print(f"Hash Table:- ")
    hash_table.print_hash_table()

    print()
    key = "Bolts"
    print(f"Value -> {key}")
    print(f"Calculated index from --> {key} is:- {hash_table.calculate_index(key)}")
    hash_table.set_value(key, "1000")
    print(f"Hash Table:- ")
    hash_table.print_hash_table()

    print()
    key = "Nails"
    print(f"Value -> {key}")
    print(f"Calculated index from --> {key} is:- {hash_table.calculate_index(key)}")
    hash_table.set_value(key, "2000")
    print(f"Hash Table:- ")
    hash_table.print_hash_table()

    print()
    key = "Saw"
    print(f"Value -> {key}")
    print(f"Calculated index from --> {key} is:- {hash_table.calculate_index(key)}")
    hash_table.set_value(key, "3000")
    print(f"Hash Table:- ")
    hash_table.print_hash_table()

    print()
    key = "Hammers"
    print(f"Value -> {key}")
    print(f"Calculated index from --> {key} is:- {hash_table.calculate_index(key)}")
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

    print()
    print(f"All Keys -> {hash_table.get_all_keys()}")

if __name__ == "__main__":
    main()