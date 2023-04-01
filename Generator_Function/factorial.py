def factorial():
    i = 1
    fact = 1
    while True:
        yield fact
        i += 1
        fact *= i


fact = factorial()
n = int(input("Enter number: "))
for next_element in range(n):
    print(next(fact))
