# Write a program to check if a number is even or odd.
number = int(input("Enter number: "))

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# Write a program to print the first 10 numbers in the Fibonacci sequence.
n = int(input("Enter n: "))
n1 = 0
n2 = 1
count = 0
if n <= 0:
    print("Enter positive number")
else:
    print("Fibonacci sequence:")
    while count < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

# Write a program to print the factorial of a number.
num = int(input("Enter number:"))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print("The factorial of", num, "is", fact)

# Write a program to find the largest of three numbers.
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))

if num1 > num2 and num1 > num3:
    largest_num = num1
elif num2 > num1 and num2 > num3:
    largest_num = num2
else:
    largest_num = num3

print("The largest number is: ", largest_num)

# Write a program to find the smallest of three numbers.
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))

if num1 < num2 and num1 < num3:
    smallest_num = num1
elif num2 < num1 and num2 < num3:
    smallest_num = num2
else:
    smallest_num = num3

print("The largest number is:", smallest_num)

# Write a program to check if a number is positive, negative, or zero.
num = int(input("Enter number: "))

if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is zero")
