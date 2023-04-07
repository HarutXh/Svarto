# lst = [200, 100, 5000, 14000, 8500, 10000, 400]
# lst2 = list(map(lambda x: x + 2000, filter(lambda x: x < 8000, lst)))
# print(lst2)


def add_2000(x):
    return x + 2000


def is_below_8000(x):
    return x < 8000


lst = [200, 100, 5000, 14000, 8500, 10000, 400]
filter_list = filter(is_below_8000, lst)
map_list = map(add_2000, filter_list)
print(list(map_list))
