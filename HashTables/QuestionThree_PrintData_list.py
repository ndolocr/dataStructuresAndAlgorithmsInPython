class HashTable:
    def __init__(self, size = 7):
        self.data_list = [None] * size
    
    def hash_values(self, word):
        my_has_key = 0
        for letter in word:
            my_has_key = (my_has_key + ord(letter) * 23)% len(self.data_list)
        return my_has_key
    
    def print_hash_table(self):
        for key, value in enumerate(self.data_list):
            print(f"{key}: {value}")

def main():
    # Initiate Hash Table
    my_hash_table = HashTable()
    hash_key_1 = my_hash_table.hash_values("Knives")    
    hash_key_2 = my_hash_table.hash_values("Spoon")
    hash_key_3 = my_hash_table.hash_values("Forks")
    hash_key_4 = my_hash_table.hash_values("Chopping_board")
    hash_key_5 = my_hash_table.hash_values("Microwave")

    print(f"Hashed value for Knives:- {hash_key_1}")
    print(f"Hashed value for Spoon:- {hash_key_2}")
    print(f"Hashed value for Forks:- {hash_key_3}")
    print(f"Hashed value for ChoppingBoard:- {hash_key_4}")
    print(f"Hashed value for Microwave:- {hash_key_5}")

    print()

    my_hash_table.print_hash_table()

if __name__ == "__main__":
    main()