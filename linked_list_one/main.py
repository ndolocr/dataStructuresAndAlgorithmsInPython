from linked_list import LinkedList

def main():
    print("="*100)

    print("LINKED LIST")
    print()
    print("Initial value:- ", end=" ")
    value = input()    

    my_linked_list = LinkedList(value)
    print()

    print()
    print("Append value 1:- ", end=" ")
    append_value_1 = input()
    my_linked_list.append(append_value_1)

    print()
    print("Append value 2:- ", end=" ")
    append_value_2 = input()
    my_linked_list.append(append_value_2)

    print()
    print("Pre-Append value:- ", end=" ")
    pre_append_value = input()
    my_linked_list.pre_append(pre_append_value)

    print()
    print(f"My Linked List:")
    print(f"Length: - {my_linked_list.lenght}")
    print(f"Linked List:- ", end="")
    print(my_linked_list.print_linked_list())

    print()
    print("POP last Node")
    my_linked_list.pop()

    print()
    print(f"My Linked List:")
    print(f"Length: - {my_linked_list.lenght}")
    print(f"Linked List:- ", end="")
    print(my_linked_list.print_linked_list())

    print()
    print("POP first Node")
    my_linked_list.front_pop()

    print()
    print(f"My Linked List:")
    print(f"Length: - {my_linked_list.lenght}")
    print(f"Linked List:- ", end="")
    print(my_linked_list.print_linked_list())

if __name__ == "__main__":
    main()