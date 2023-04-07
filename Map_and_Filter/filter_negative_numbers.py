def is_negative(n):
    return n < 0


numbers = (-2, 5, 8, -23, -4)
result = filter(is_negative, numbers)
print(list(result))
