class HashTable:
    def __init__(self, size = 7):
        self.list_item = [None] * size
    
    def print_hash_table(self):
        for key, value in enumerate(self.list_item):
            print(f"{key} : {value}")
        return self.list_item
    
    def calculate_hash_key(self, key):
        hashed_value = 0

        for letter in key:
            hashed_value = (hashed_value + ord(letter) * 23) % len(self.list_item)
        return hashed_value
    
    def set_value(self, key, value):
        index = self.calculate_hash_key(key)
        if self.list_item[index] is None:
            self.list_item[index] = []
        self.list_item[index].append([key, value])
        return [index, value]

def main():
    # Initiate Hash Table
    hash_table = HashTable()
    print(f"Hash Table --> {hash_table}")

    print()
    key = "Bolts"
    print(f"Value -> {key}")
    print(f"Calculated index from --> {key} is:- {hash_table.calculate_hash_key(key)}")
    hash_table.set_value(key, "1000")
    print(f"Hash Table:- ")
    hash_table.print_hash_table()

    print()
    key = "Nails"
    print(f"Value -> {key}")
    print(f"Calculated index from --> {key} is:- {hash_table.calculate_hash_key(key)}")
    hash_table.set_value(key, "2000")
    print(f"Hash Table:- ")
    hash_table.print_hash_table()

    print()
    key = "Saw"
    print(f"Value -> {key}")
    print(f"Calculated index from --> {key} is:- {hash_table.calculate_hash_key(key)}")
    hash_table.set_value(key, "3000")
    print(f"Hash Table:- ")
    hash_table.print_hash_table()

    print()
    key = "Hammers"
    print(f"Value -> {key}")
    print(f"Calculated index from --> {key} is:- {hash_table.calculate_hash_key(key)}")
    hash_table.set_value(key, "2000")
    print(f"Hash Table:- ")
    hash_table.print_hash_table()

if __name__ == "__main__":
    main()