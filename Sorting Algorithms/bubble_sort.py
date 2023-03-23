def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


lst = [5, 4, 3, 1, 2]
bubble_sort(lst)
for i in range(len(lst)):
    print(lst[i], end="")
