def sentinel_search(el, lst):
    size = len(lst)
    lst.append(el)
    i = 0
    while lst[i] != el:
        i += 1
    if i == size:
        return -1
    else:
        return f"index of {el} is {i}"


lst = [5, 8, 64, 852, 24]
el = int(input("Enter element: "))
print(sentinel_search(el, lst))
