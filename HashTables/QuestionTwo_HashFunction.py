class HashTable:
    def __init__(self, size = 7):
        self.data_map_list = [None] * size
    

    def _hash(self, key):
        my_hash = 0

        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map_list)
        return my_hash

def main():
    # Initiate Hash Table
    my_table = HashTable(13)
    hash_value = my_table._hash("Spoon")
    print(f"Hash for 'Spoon' :- {hash_value}")

if __name__ == "__main__":
    main()