# Write a program to convert Celsius to Fahrenheit.
celsius = 37.5
fahrenheit = (celsius * 1.8) + 32
print(
    "%0.1f degree Celsius is equal to %0.1f degree Fahrenheit" % (celsius, fahrenheit)
)
# Write a program to convert Fahrenheit to Celsius.
fahrenheit = 90.5
celsius = (fahrenheit - 32) / 1.8
print(
    "%0.1f degree Fahrenheit is equal to %0.1f degree Celsius" % (fahrenheit, celsius)
)

# Write a program to convert kilometers to miles.
kilometers = float(input("Enter value in kilometers: "))
conv_fac = 0.621371
miles = kilometers * conv_fac
print("%0.2f kilometers is equal to %0.2f miles" % (kilometers, miles))

# Write a program to convert miles to kilometers.
miles = float(input("Enter value in kilometers: "))
conv_fac = 0.621371
kilometers = miles / conv_fac
print("%0.2f miles is equal to %0.2f kilometers" % (miles, kilometers))
