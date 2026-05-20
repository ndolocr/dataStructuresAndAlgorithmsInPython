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

    print("Pre-append the value 5 in the linked list")
    singly_linked_list.preappend(5)
    print("Print List after pre-appending 5")
    singly_linked_list.print_linked_list()
    print()

    print("Pre-append the value 4 in the linked list")
    singly_linked_list.preappend(4)
    print("Print List after pre-appending 5")
    singly_linked_list.print_linked_list()
    print()

    print("Pre-append the value 3 in the linked list")
    singly_linked_list.preappend(3)
    print("Print List after pre-appending 5")
    singly_linked_list.print_linked_list()
    print()

    print("Pre-append the value 2 in the linked list")
    singly_linked_list.preappend(2)
    print("Print List after pre-appending 5")
    singly_linked_list.print_linked_list()
    print()

    print("POP the linked list")
    singly_linked_list.pop()
    print("Print List Popping tail")
    singly_linked_list.print_linked_list()
    print()

    print("Get Value at index 1")
    singly_linked_list.get_by_index(1)
    print()

    print("Update Value at index 1")
    singly_linked_list.change_node_value_by_index(1, "n")
    print()

    print("Inserting New Node at index 1")
    singly_linked_list.insert_value(1, "i")
    print()

    print("Print List after updating node")
    singly_linked_list.print_linked_list()
    print()

    print("Remove New Node at index 2")
    singly_linked_list.remove_node(2)
    print()

    print("Print List after updating node")
    singly_linked_list.print_linked_list()
    print()

    print("Reverse the Linked List")
    singly_linked_list.reverse_list()
    print()

    print("Print List after reversing Linked List")
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

    print("Get Value at index 1")
    doubly_linked_list.get_node_by_index(1)
    print()


    print("Update Value at index 1")
    doubly_linked_list.change_node_value_by_index(1, "n")
    print()

    print("Inserting New Node at index 1")
    doubly_linked_list.insert_value(1, "x")
    print()

    print("Print List after updating node")
    doubly_linked_list.print_linked_list()
    print()

    print("Remove New Node at index 2")
    doubly_linked_list.remove_node(2)
    print()

    print("Print List after updating node")
    doubly_linked_list.print_linked_list()
    print()

if __name__ == "__main__":
    main()