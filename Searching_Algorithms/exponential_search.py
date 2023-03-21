def exponential_search(lst, x):
    if lst[0] == x:
        return 0
    i = 1
    while i < len(lst) and lst[i] <= x:
        i *= 2
    return binary_search(lst, x, i // 2, len(lst) - 1)


def binary_search(lst, x, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        if lst[mid] == x:
            return f"Index of {x} is {mid}"
        elif lst[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    else:
        return -1


lst = [11, 12, 13, 14, 15, 16, 17, 18, 19]
x = int(input("Enter number: "))
print(exponential_search(lst, x))
