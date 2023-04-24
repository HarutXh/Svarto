# Write a program to find the GCD (Greatest Common Divisor) of two numbers.
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
while n1 != n2:
    if n1 > n2:
        n1 -= n2
    else:
        n2 -= n1
print("GCD = ", n1)

# Write a program to find the LCM (Least Common Multiple) of two numbers.
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
if n1 > n2:
    larger = n1
else:
    larger = n2
for i in range(larger, 1 + (n1 * n2)):
    if i % n1 == i % n2 == 0:
        lcm = i
        break
print("LCM = ", lcm)

# Write a program to convert a decimal number to a binary number.
dec = int(input("Enter a decimal number: "))
binary = ""

while dec > 0:
    binary = str(dec % 2) + binary
    dec = dec // 2

print("Binary equivalent = ", binary)

# Write a program to convert a decimal number to a hexadecimal number.
dec = int(input("Enter a decimal number: "))
hexa = ""

while dec > 0:
    rem = dec % 16
    if rem < 10:
        hexa = str(rem) + hexa
    else:
        hexa = chr(rem - 10 + ord("A")) + hexa
    dec = dec // 16

print("Hexadecimal equivalent = ", hexa)

# Write a program to convert a binary number to a decimal number.
binary = input("Enter a binary number: ")
decimal = 0
power = len(binary) - 1

for digit in binary:
    decimal += int(digit) * 2**power
    power -= 1

print("Decimal equivalent = ", decimal)

# Write a program to convert a binary number to a hexadecimal number.
binary = input("Enter a binary number: ")
decimal = 0
power = len(binary) - 1
for digit in binary:
    decimal += int(digit) * 2**power
    power -= 1
hexa = ""
while decimal > 0:
    remainder = decimal % 16
    if remainder < 10:
        hexa = str(remainder) + hexa
    else:
        hexa = chr(remainder + 55) + hexa
    decimal //= 16

print("Hexadecimal equivalent = ", hexa)


# Write a program to convert a hexadecimal number to a decimal number.
hexa = input("Enter a hexadecimal number: ")

decimal = 0
power = len(hexa) - 1

for digit in hexa:
    if ord(digit) >= 48 and ord(digit) <= 57:  # if digit is between 0-9 in ASCII table
        decimal += (ord(digit) - 48) * 16**power
    elif (
        ord(digit) >= 65 and ord(digit) <= 70
    ):  # if digit is between A-F in ASCII table
        decimal += (ord(digit) - 55) * 16**power
    elif (
        ord(digit) >= 97 and ord(digit) <= 102
    ):  # if digit is between a-f in ASCII table
        decimal += (ord(digit) - 87) * 16**power
    else:
        print("Invalid hexadecimal number!")
        exit()

    power -= 1

print("Decimal equivalent = ", decimal)

# Write a program to convert a hexadecimal number to a binary number.
hexa = input("Enter a hexadecimal number: ")

binary = ""
for digit in hexa:
    binary += format(int(digit, 16), "04b")

print("Binary equivalent = ", binary)

# Write a program to check if a number is a prime number.
num = int(input("Enter a number: "))
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

# Write a program to generate all prime numbers up to a given number.
num = int(input("Enter number: "))
for num in range(num + 1):
    # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")


# Write a program to find the factorial of a number using recursion.
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


num = int(input("Enter number: "))

# check if the number is negative
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))


# Write a program to find the sum of the digits of a number.
def digit_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


n = int(input("Enter a number: "))
print("The sum of digits of", n, "is", digit_sum(n))

# Write a program to find the reverse of a number.
num = int(input("Enter number:"))
reverse_num = 0
while num != 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num //= 10
print("Reverse of the number", reverse_num)

# Write a program to check if a number is a palindrome.
number = int(input("Enter number:"))
last_digit = number % 10
second_digit = number // 10 % 10
first_digit = number // 100
reverse = last_digit * 100 + second_digit * 10 + first_digit
is_palindrome_or_not = reverse == number
print(is_palindrome_or_not)

# Write a program to find the factors of a number.
num = int(input("Enter number: "))
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
