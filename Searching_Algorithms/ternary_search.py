def ternary_search(lst, left, right, el):
    if left > right:
        return -1
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3
    if lst[mid1] == el:
        return mid1
    if lst[mid2] == el:
        return mid2
    if el < lst[mid1]:
        return ternary_search(lst, left, mid1 - 1, el)
    elif el > lst[mid2]:
        return ternary_search(lst, mid2 + 1, right, el)
    else:
        return ternary_search(lst, mid1 + 1, mid2 - 1, el)


lst = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
left = int(input("Enter number left: "))
right = int(input("Enter number right: "))
el = int(input("Enter number element: "))
result = ternary_search(lst, left, right, el)

if result != -1:
    print(f"Element {el} is present at index {result}")
else:
    print(f"Element {el} is not present in list")
