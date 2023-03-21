def binary_search(lst, el, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if lst[mid] == el:
            return mid
        elif lst[mid] < el:
            low = mid + 1
        else:
            high = mid - 1
    return -1


lst = [7, 8, 9, 10, 11, 12, 13, 14]
el = int(input("Enter element: "))
result = binary_search(lst, el, 0, len(lst) - 1)

if result != -1:
    print(f"Element {el} is present at index {result}")
else:
    print(f"Element {el} is not present in list")
