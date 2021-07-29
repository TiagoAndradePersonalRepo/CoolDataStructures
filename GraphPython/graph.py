from typing import Generic, TypeVar
from SortedListPython.sortedList import SortedList
from GraphPython.addable import Addable

V = TypeVar('V')
class Graph(Generic[V]) :

    def __init__(self, directed : bool = True) :
        self.__graph_dict = {}
        self.__directed = directed

    def insertEdge(self, originVertex : V, targetVertex : V, edgeValue : Addable) :
        self.__insertVertex(originVertex)
        self.__insertVertex(targetVertex)

        self.__graph_dict[originVertex].append((edgeValue, targetVertex)) # {targetVertex : edgeValue})
        if not self.__directed :
            self.__graph_dict[targetVertex].append((edgeValue, originVertex)) # {originVertex : edgeValue})
    
    def __insertVertex(self, vertex : V) :
        if not vertex in self.__graph_dict :
            self.__graph_dict[vertex] = SortedList()         

    def __str__(self) :
        return str(self.__graph_dict)

    def shortestPath(self, originVertex : V, targetVertex : V) :
        all_lists = SortedList()
        (cost, topVert, path) = (0, originVertex, [])
        new_list = [originVertex]

        while not topVert.__eq__(targetVertex):
            for adjCost, adjVert in self.__graph_dict[topVert] :

                if adjVert not in path :
                    new_tup = (adjCost.__add__(cost), adjVert, new_list)
                    all_lists.append(new_tup)

            (cost, topVert, path) = all_lists.pop(0)
            new_list = path.copy()
            new_list.append(topVert) 

        return (new_list, cost)