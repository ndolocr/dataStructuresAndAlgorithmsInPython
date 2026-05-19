from SinglyLinkedList.SinglyLinkedList import SinglyLinkedList
from DoublyLinkedList.DoublyLinkedList import DoublyLinkedList

def main():
    print("SINGLY LIKNED LIST")
    print()
    print("List initiation")
    singly_linked_list = SinglyLinkedList(6)

    singly_linked_list.print_linked_list()

    ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    print("-"*150) 
    print("DOUBLY LIKNED LIST")
    print()
    print("List initiation")
    doubly_linked_list = DoublyLinkedList(6)

    doubly_linked_list.print_linked_list()


if __name__ == "__main__":
    main()