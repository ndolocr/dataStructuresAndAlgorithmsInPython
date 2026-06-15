class HashTable:
    def __init__(self, size = 7):
        self.list_item = [None] * size
    
    def print_hash_table(self):
        for key, value in enumerate(self.list_item):
            print(f"{key}: {value}")

def main():
    # Initiate Hash Table
    hash_table = HashTable()
    hash_table.print_hash_table()

if __name__ == "__main__":
    main()