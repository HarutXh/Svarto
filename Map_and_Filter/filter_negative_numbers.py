def is_negative(n):
    if n < 0:
        return True
    else:
        return False


numbers = (-2, 5, 8, -23, -4)
result = filter(is_negative, numbers)
print(list(result))
