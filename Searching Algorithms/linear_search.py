def linear_search(el, lst):
    for i in range(len(lst)):
        if lst[i] == el:
            return f"index of {el} is {i}"
    return -1


lst = [5, 15, 85, 477]
el = int(input("Enter element: "))
print(linear_search(el, lst))
