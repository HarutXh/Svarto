def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
size = int(input("Enter size: "))
for i in range(size):
    print(next(fib))
