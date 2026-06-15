class HashTable:
    def __init__(self, size = 7):
        self.list_item = [None] * size

    def print_hash_map(self):
        for key, value in enumerate(self.list_item):
            print(f"{key} : {value}")

    def hash_key(self, key):
        my_hash_key = 0
        for letter in key:
            my_hash_key = (my_hash_key + ord(letter) * 23) % len(self.list_item)
        return my_hash_key

def main():
    # Inititate Hash Map
    my_hash_table = HashTable()

    # Print Hash Table
    my_hash_table.print_hash_map()

    # Generate hashed value for Keyword German
    print(f"Hash Value for (Bolts) is:- {my_hash_table.hash_key('Bolts')}")

if __name__ == "__main__":
    main()