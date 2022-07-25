from bst import BinarySearchTree

def test_bst1() :
    bst = BinarySearchTree()
    for i in [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15] :
        bst.addNode(i)

    print(bst.getRoot())
    print()
    print(bst)
    print()
    print(bst.nodesByLevel())
    #print(bst.inOrder())
    #print(bst.preOrder())
    #print(bst.posOrder())

def test_bst2() :
    bst = BinarySearchTree()
    for i in [8, 4, 13, 2, 6, 10, 15, 1, 3, 5, 7, 9, 11, 14, 16, 12] :
        bst.addNode(i)

    print(bst.getRoot())
    print()
    print(bst)
    print()
    print(bst.nodesByLevel())
    print()
    print(bst.nodesByLevel2())
    print()
    print(bst.nodesByLevel3())

def test_bst3() :
    bst = BinarySearchTree()
    for i in range(5, 1, -1) :
        bst.addNode(i)

    print(bst.nodesByLevel3())

def main() :
    # test_bst1()
    test_bst2()
    test_bst3()

if __name__ == "__main__" :
    main()
