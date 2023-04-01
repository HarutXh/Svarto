def my_range():
    a = 0
    while True:
        yield a
        a += 1


myRange = my_range()
n = int(input("Enter number: "))
for next_element in range(n):
    print(next(myRange))
