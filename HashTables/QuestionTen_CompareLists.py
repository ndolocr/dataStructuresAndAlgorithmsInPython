def main():
    list_1 = [2, 3, 4, 5]
    list_2 = [8, 7, 6, 5]

    my_dict = {}
    for i in list_1:
        my_dict[i] = True

    for j in list_2:
        if j in my_dict:
            print([i, i])

if __name__ == "__main__":
    main()