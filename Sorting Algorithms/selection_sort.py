def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]


lst = [5, 4, 3, 1, 2, 8, 6, 7]
selection_sort(lst)
for i in range(len(lst)):
    print(lst[i], end="")
