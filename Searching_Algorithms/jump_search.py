def jump_search(lst, x):
    n = len(lst)
    step = int(n**0.5)
    prev = 0
    while lst[step - 1] < x:
        prev = step
        step += int(n**0.5)
        if prev >= n:
            return -1
    while lst[prev] < x:
        prev += 1
        if prev == step:
            return -1
    if lst[prev] == x:
        return f"Index of {x} is {prev}"
    return -1


lst = [11, 12, 13, 14, 15, 16, 17, 18, 19]
x = int(input("Enter number: "))
print(jump_search(lst, x))
