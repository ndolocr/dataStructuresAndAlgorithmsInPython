from PythonList import PythonListClass

def main():
    mylist = PythonListClass("a")
    mylist.list_append("c")
    mylist.list_insert(1, "b")

    second_list = ["d", "e", "f"]
    mylist.list_extend(second_list)
    mylist.print_full_list()

if __name__=="__main__":
    main()