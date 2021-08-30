from sortedList import SortedList

def main() :
    sl1 = SortedList()
    sl1.append(4)
    print(sl1)

    sl1.append(1)
    print(sl1)

    sl1.append(2)
    print(sl1)

    print()

    sl2 = SortedList([4, 1, 2])
    print(sl2)

    print()

    sl3 = SortedList([4, 1, 2], False)
    print(sl3)

    print()

    sl4 = SortedList([4, 1, 3, 2, 1], unique = True)
    print(sl4)

    sl4.reverse()
    print(sl4)

    sl4.append(7)
    print(sl4)

    print()

    sl5 = SortedList([(4, "A"), (3, "E"), (2, "C"), (2, "D"), (1, "B")])
    print(sl5)

    print()

    for i in sl5 :
        print(i)

    print()
    print(sl5[2])

if __name__ == "__main__" :
    main()
