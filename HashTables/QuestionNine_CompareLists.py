def main():
    # Compare if the two lists have an item in common

    list_1 = [2, 3, 4, 5]
    list_2 = [8, 7, 6, 5]

    # Bad Algorithm 0(n2)

    for x in list_1:
        for y in list_2:
            if x == y:
                print( [x, y] )

if __name__ == "__main__":
    main()
            