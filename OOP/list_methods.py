class MyList:
    def __init__(self, lst):
        self.__lst = lst

    def append(self, element):
        self.__lst += [element]
        return self.__lst

    def clear(self):
        self.__lst = []
        return self.__lst

    def copy(self):
        return self.__lst[:]

    def count(self, item):
        count = 0
        for elem in self.__lst:
            if elem == item:
                count += 1
        return count

    def extend(self, other):
        self.__lst += other
        return self.__lst

    def index(self, item):
        for i in range(len(self.__lst)):
            if self.__lst[i] == item:
                return i
        raise ValueError(f"{item} is not in list")

    def insert(self, index, element):
        self.__lst = self.__lst[:index] + [element] + self.__lst[index:]
        return self.__lst

    def pop(self, index=-1):
        if not self.__lst:
            raise IndexError("pop from empty list")
        if index < 0:
            index += len(self.__lst)
        if index < 0 or index >= len(self.__lst):
            raise IndexError("pop index out of range")
        del self.__lst[index]
        return self.__lst

    def remove(self, value):
        if not self.__lst:
            raise ValueError("list.remove(x): x not in list")
        for i in range(len(self.__lst)):
            if self.__lst[i] == value:
                del self.__lst[i]
                return
        raise ValueError("list.remove(x): x not in list")

    def reverse(self):
        return self.__lst[::-1]

    def sort(self):
        for i in range(len(self.__lst)):
            for j in range(i + 1, len(self.__lst)):
                if self.__lst[i] > self.__lst[j]:
                    self.__lst[i], self.__lst[j] = self.__lst[j], self.__lst[i]
        return self.__lst


if __name__ == "__main__":
    lst = MyList([4, 8, 10, 7, 9, 8, 9, 10])
    print(lst.copy())
    print(lst.index(8))
    print(lst.count(9))
    print(lst.extend([2, 1, 6]))
    print(lst.append(11))
    print(lst.insert(1, 2))
    print(lst.pop())
    lst.remove(8)
    print(lst._MyList__lst)
    print(lst.reverse())
    print(lst.sort())
    print(lst.clear())
