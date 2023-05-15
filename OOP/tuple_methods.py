class MyTuple:
    def __init__(self, tpl):
        self.__tpl = tpl

    def count(self, item):
        count = 0
        for element in self.__tpl:
            if element == item:
                count += 1
        return count

    def index(self, value, start=0, end=-1):
        if end == -1:
            end = len(self.__tpl)
        for i in range(start, end):
            if self.__tpl[i] == value:
                return i
        raise ValueError(f"{value} is not in tuple")


if __name__ == "__main__":
    tpl = MyTuple((1, 2, 2, 3, 3, 4))
    print(tpl.count(1))
    print(tpl.index(3))
