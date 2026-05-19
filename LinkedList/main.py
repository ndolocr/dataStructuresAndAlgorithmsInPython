from SinglyLinkedList.SinglyLinkedList import SinglyLinkedList
from DoublyLinkedList.DoublyLinkedList import DoublyLinkedList

def main():
    print("SINGLY LIKNED LIST")
    print()
    print("List initiation")
    singly_linked_list = SinglyLinkedList(6)
    print("Print original List")
    singly_linked_list.print_linked_list()
    print()

    print("Append the value 8 in the linked list")
    singly_linked_list.append(8)
    print("Print List after appending 8")
    singly_linked_list.print_linked_list()
    print()

    print("Pre-ppend the value 5 in the linked list")
    singly_linked_list.preappend(5)
    print("Print List after pre-appending 5")
    singly_linked_list.print_linked_list()
    print()

    ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    print("-"*150) 
    print("DOUBLY LIKNED LIST")
    print()
    print("List initiation")
    print("Print original List")
    doubly_linked_list = DoublyLinkedList(6)
    doubly_linked_list.print_linked_list()
    print()

    print("Append the value 8 in the linked list")
    doubly_linked_list.append(8)
    print("Print List after appending 8")
    doubly_linked_list.print_linked_list()
    print()

    print("Pre-append the value 5 in the linked list")
    doubly_linked_list.preappend(5)
    print("Print List after pre-appending 5")
    doubly_linked_list.print_linked_list()
    print()


if __name__ == "__main__":
    main()