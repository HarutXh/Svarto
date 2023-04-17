# Write a program to find the area of a triangle.
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

p = (a + b + c) / 2

area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print("The area of the triangle is %0.2f" % area)

# Write a program to find the area of a rectangle.
width = float(input("Enter width length: "))
height = float(input("Enter height weight: "))
area = width * height
print("The rectangle area is:", area)

# Write a program to find the perimeter of a rectangle.
width = float(input("Enter width length: "))
height = float(input("Enter height weight: "))
perimeter = 2 * (width + height)
print("The rectangle perimeter is:", perimeter)

# Write a program to find the circumference of a circle.
r = float(input("Enter radius: "))
pi = 3.14
length = 2 * pi * r
print("Circumference of a circle is:", length)

# Write a program to find the area of a circle.
r = float(input("Enter radius: "))
pi = 3.14
area = pi * r**2
print("Circumference of a circle is:", area)

# Write a program to find the volume of a sphere.
r = float(input("Enter radius: "))
pi = 3.14
area = (4.0 / 3.0) * pi * r**3
print("Circumference of a circle is:", area)

# Write a program to find the volume of a cylinder.
height = int(input("Enter height length: "))
r = int(input("Enter radius: "))
pi = 3.14
volume = pi * r**2 * height
print("Volume of a cylinder is:", volume)
