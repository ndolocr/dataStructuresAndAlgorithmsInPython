from SinglyLinkedListExerciseFolder.LinkedList import LinkedList

def main():
    linked_list = LinkedList(1)

    # Append Values
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(6)
    linked_list.append(7)
    linked_list.append(8)
    linked_list.append(9)
    linked_list.append(10)

    linked_list.print_linked_list()

    linked_list.get_middle_node()

if __name__ == "__main__":
    main()