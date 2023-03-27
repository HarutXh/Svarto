def interpolation_search(lst, x):
    low = 0
    high = len(lst) - 1
    while low <= high and x >= lst[low] and x <= lst[high]:
        pos = low + ((x - lst[low]) * (high - low)) // (lst[high] - lst[low])
        if lst[pos] == x:
            return f"Index of {x} is {pos}"
        elif lst[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return -1


lst = [11, 12, 13, 14, 15, 16, 17, 18, 19]
x = int(input("Enter number: "))
print(interpolation_search(lst, x))
