class Square:
    def __init__(self, side, color):
        # self.side = side
        self.set_side(side)
        self.color = color

    def get_area(self):
        return self.__side**2

    def get_perimeter(self):
        return 4 * self.__side

    def get_side(self):
        return self.__side

    def set_side(self, side):
        if side > 0:
            self.__side = side
        else:
            self.__side = 0

    def draw_square(self, symbol):
        for row in range(0, self.__side):
            for column in range(0, self.__side):
                if (
                    row == 0
                    or row == self.__side - 1
                    or column == 0
                    or column == self.__side - 1
                ):
                    print(f"{symbol}", end=" ")
                else:
                    print(" ", end=" ")
            print()


square1 = Square(5, "green")

print("Square color is", square1.color)
print("Square area is", square1.get_area())
print("Square perimeter is", square1.get_perimeter())
print(square1.get_side())
square1.draw_square("*")
square1.set_side(8)
print(square1.get_side())
square1.draw_square("/")
