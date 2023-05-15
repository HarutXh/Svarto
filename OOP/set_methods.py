class MySet:
    def __init__(self, st):
        self.__st = st

    def add(self, element):
        if element not in self.__st:
            self.__st |= {element}
        return self.__st

    def clear(self):
        self.__st = {}
        return self.__st

    def copy(self):
        new_set = MySet(set())
        for element in self.__st:
            new_set.add(element)
        return new_set.__st

    def difference(self, other_set):
        return MySet(self.__st - other_set)

    def difference_update(self, other):
        return self.__st - other

    def discard(self, element):
        if element in self.__st:
            self.__st -= {element}
        return self.__st

    def intersection(self, other):
        return MySet(self.__st & other)

    def intersection_update(self, other):
        return MySet(self.__st & other)

    def isdisjoint(self, other_set):
        for element in other_set:
            if element in self.__st:
                return False
        return True

    def issubset(self, other_set):
        for element in self.__st:
            if element not in other_set:
                return False
        return True

    def is_superset(self, other_set):
        for element in other_set:
            if element not in self.__st:
                return False
        return True

    def pop(self):
        if not self.__st:
            raise KeyError("pop from an empty set")
        element = next(iter(self.__st))
        self.__st = self.__st - {element}
        return self.__st

    def remove(self, element):
        if element in self.__st:
            self.__st -= {element}
        else:
            raise KeyError(f"{element} not found in set")
        return self.__st

    def symmetric_difference(self, other_set):
        return MySet(self.__st ^ other_set.__st)

    def symmetric_difference_update(self, other_set):
        return MySet(self.__st ^ other_set.__st)

    def union(self, other):
        return MySet(self.__st | other.__st)

    def update(self, other):
        return MySet(self.__st | other.__st)


if __name__ == "__main__":
    st = MySet(set([1, 5, 7, 3, 6, 4]))
    st2 = MySet(set([7, 5, 3]))
    print(st.issubset(set([7, 5, 3])))
    print(st.isdisjoint(set([8, 9, 10])))
    print(st.is_superset(set([7, 5, 3])))
    print(st.symmetric_difference(st2)._MySet__st)
    print(st.symmetric_difference_update(st2)._MySet__st)
    print(st.union(st2)._MySet__st)
    print(st.update(st2)._MySet__st)
    print(st.pop())
    print(st.remove(3))
    print(st.add(8))
    print(st.copy())
    print(st.intersection(set([2, 3, 4]))._MySet__st)
    print(st.intersection_update(set([2, 3, 4]))._MySet__st)
    print(st.difference(set([2, 3, 4]))._MySet__st)
    print(st.difference_update(set([2, 3, 4])))
    print(st.discard(5))
    print(st.clear())
