# Write a program to find the roots of a quadratic equation.
print("Quadratic function : (a * x^2) + b*x + c")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
discriminant = b**2 - 4 * a * c

if discriminant > 0:
    x1 = (-b) + (0.5 ** (discriminant)) / (2 * a)
    x2 = (-b) - (0.5 ** (discriminant)) / (2 * a)
    print("There are 2 roots: %f and %f" % (x1, x2))

elif discriminant == 0:
    x = (-b) / (2 * a)
    print("There is one root: ", (x))

else:
    print("No Roots, Discriminant < 0")

# Write a program to check if a year is a leap year.
year = int(input("Enter number: "))

if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
    print("Given year is a leap year")
else:
    print(("Given year is not leap year"))

# Write a program to generate a random number.
import random

print(random.randint(0, 100))
