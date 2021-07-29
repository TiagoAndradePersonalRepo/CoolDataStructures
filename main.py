from GraphPython.graph import Graph
from SortedListPython.sortedList import SortedList
from GraphPython.addable import Addable

class Car() :
    def __init__(self, brand, year) :
        self.brand = brand
        self.year = year

car = Car("Ferrari", 2021)

def test_sorted_list() :
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

def create_graph1() :
    g = Graph[str]()
    
    g.insertEdge("A", "B", 2)
    g.insertEdge("A", "C", 3)
    g.insertEdge("D", "B", 1)
    g.insertEdge("E", "F", 7)
    g.insertEdge("A", "E", 4)

    return g

def create_graph2() :
    g = Graph[str]()
    
    g.insertEdge("A", "E", 4)
    g.insertEdge("A", "C", 3)

    g.insertEdge("B", "A", 2)
    g.insertEdge("B", "D", 7)

    g.insertEdge("C", "H", 20)

    g.insertEdge("D", "F", 3)

    g.insertEdge("E", "D", 6)
    g.insertEdge("E", "F", 10)
    g.insertEdge("E", "C", 8)

    g.insertEdge("F", "G", 1)

    g.insertEdge("G", "E", 1)
    g.insertEdge("G", "I", 2)

    g.insertEdge("H", "G", 4)

    g.insertEdge("I", "H", 3)

    return g

def create_graph3() :
    g = Graph[str]()
    
    g.insertEdge("A", "B", 5)
    g.insertEdge("A", "C", 20)
    g.insertEdge("B", "C", 6)

    return g

def invalid_graph() :
    g = Graph[str]()
    g.insertEdge("A", "B", car)

def test_graphs() :
    g1 = Graph(car)
    print(g1)

    g2 = create_graph2()
    print(g2)
    print()
    print(g2.shortestPath("A", "I"))
    print()
    g3 = create_graph3()
    print(g3)
    print()
    print(g3.shortestPath("A", "C"))

    invalid_graph()

def test_addable() :
    print(isinstance(car, Addable))

def main() :
    test_sorted_list()
    test_addable()
    test_graphs()

if __name__ == "__main__" :
    main()
