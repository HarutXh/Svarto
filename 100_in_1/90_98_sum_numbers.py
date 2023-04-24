# # Write a program to find the sum of the first n natural numbers.
# n = int(input("Enter number:"))
# sum = 0
# for i in range(1, n + 1):
#     sum+=i
# print(sum)

# # Write a program to find the sum of the first n even numbers.
# n = int(input("Enter number:"))
# sum = 0
# for i in range(0, n + 1, 2):
#     psum+=i
# print(sum)

# # Write a program to find the sum of the first n odd numbers.
# n = int(input("Enter number:"))
# sum = 0
# for i in range(0, n + 1, 2):
#     sum += i
# print(sum)

# # Write a program to find the sum of the squares of the first n natural numbers.
# n = int(input("Enter number:"))
# sum = 0
# for i in range(1, n + 1):
#     sum += i**2
# print(sum)

# # Write a program to find the sum of the cubes of the first n natural numbers.
# n = int(input("Enter number:"))
# sum = 0
# for i in range(1, n + 1):
#     sum += i**3
# print(sum)

# # Write a program to find the sum of the series 1/1! + 2/2! + 3/3! + ... + n/n!.
# n = int(input("Enter number:"))
# sum = 0
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
#     sum += i / fact
# print(sum)

# # Write a program to find the sum of the series 1^2 + 2^2 + 3^2 + ... + n^2.
# n = int(input("Enter number:"))
# sum = 0
# for i in range(1, n + 1):
#     sum += i**2
# print(sum)

# # Write a program to find the sum of the series 1/1^2 + 1/2^2 + 1/3^2 + ... + 1/n^2.
# n = int(input("Enter number:"))
# sum = 0
# for i in range(1, n + 1):
#     sum += 1 / (i**2)
# print(sum)

# # Write a program to find the sum of the series 1 + x + x^2 + x^3 + ... + x^n.
# x = float(input("Enter the value of x: "))
# n = int(input("Enter the value of n: "))
# sum = 0
# for i in range(n):
#     term = x**i
#     sum += term
# print("The sum of the series is:", sum)
