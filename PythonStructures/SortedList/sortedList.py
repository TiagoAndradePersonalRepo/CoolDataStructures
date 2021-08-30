from collections import Iterable

class SortedList(Iterable) :

    def __init__(self, initial_list = [], descending = True, unique = False) :
        self.__list = []
        self.__descending = descending
        self.__unique = unique
        self.extend(initial_list)

    def append(self, value) :
        size = len(self.__list)
        if size == 0 :
            self.__list.append(value)
        else :
            for i in range(size) :
                elem = self.__list[i]

                if value.__eq__(elem) :
                    if not self.__unique :
                        self.__list.insert(i, value)
                    break

                elif value.__lt__(elem):
                    if self.__descending :
                        self.__list.insert(i, value)
                    else :
                        self.__list.insert(i + 1, value)
                    break
                
                elif i == size - 1 and self.__descending : # reorganize
                    self.__list.append(value)

                elif i == 0 and not self.__descending : # reorganize
                    self.__list.insert(i, value)

    def clear(self) :
        self.__list.clear()

    def copy(self) :
        nl = SortedList()
        nl.__list.extend(self.__list.copy())
        return nl

    def count(self, value) :
        return self.__list.count(value)

    def extend(self, iterable) :
        for elem in iterable :
            self.append(elem)

    def index(self, value) :
        return self.__list.index(value)

    def pop(self, index) :
        return self.__list.pop(index)

    def remove(self, value) :
        self.__list.remove(value)

    def reverse(self) : # remake in O(n)
        if self.__descending :
            self.__list.reverse()
        else :
            self.__list.sort() 

        self.__descending = not self.__descending

    def __repr__(self) :
        return self.__list.__repr__()

    def __cmp__(self, other) :
        return self.__list.cmp(other)

    def __iter__(self) :
        for i in self.__list :
            yield i

    def __getitem__(self, key) :
        return self.__list[key]

    def __len__(self) :
        return len(self.__list)