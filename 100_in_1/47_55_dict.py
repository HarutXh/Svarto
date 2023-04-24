# Write a program to find the sum of all the elements in a dictionary.
dct = {"x": 300, "y": 400, "z": 840, "u": 524}
sum = 0
for item in dct.values():
    sum += item
print(sum)

# Write a program to find the product of all the values in a dictionary.
dct = {"x": 30, "y": 40, "z": 84, "u": 5}
mult = 1
for item in dct.values():
    mult *= item
print(mult)

# Write a program to find the largest value in a dictionary.
dct = {"x": 30, "y": 40, "z": 84, "u": 5}
max_value = max(dct.values())
print(max_value)

# Write a program to find the smallest value in a dictionary.
dct = {"x": 30, "y": 40, "z": 84, "u": 5}
max_value = min(dct.values())
print(max_value)

# Write a program to sort a dictionary by its keys in ascending order.
dct = {"z": 30, "x": 40, "y": 84, "u": 5}
keys = []

for key in dct:
    keys.append(key)

n = len(keys)
for i in range(n):
    for j in range(0, n - i - 1):
        if keys[j] > keys[j + 1]:
            keys[j], keys[j + 1] = keys[j + 1], keys[j]

sorted_dict = {}
for key in keys:
    sorted_dict[key] = dct[key]
print(sorted_dict)

# Write a program to sort a dictionary by its keys in descending order.
dct = {"z": 30, "x": 40, "y": 84, "u": 5}
keys = []

for key in dct:
    keys.append(key)

n = len(keys)
for i in range(n):
    for j in range(0, n - i - 1):
        if keys[j] < keys[j + 1]:
            keys[j], keys[j + 1] = keys[j + 1], keys[j]

sorted_dict = {}
for key in keys:
    sorted_dict[key] = dct[key]
print(sorted_dict)

# Write a program to sort a dictionary by its values in ascending order.
dct = {"z": 30, "x": 40, "y": 84, "u": 5}
values = []

for value in dct:
    values.append(value)

n = len(dct)
for i in range(n):
    for j in range(0, n - i - 1):
        if dct[values[j]] > dct[values[j + 1]]:
            values[j], values[j + 1] = values[j + 1], values[j]

sorted_dict = {}
for value in values:
    sorted_dict[value] = dct[value]
print(sorted_dict)

# Write a program to sort a dictionary by its values in descending order.
dct = {"z": 30, "x": 40, "y": 84, "u": 5}
values = []

for value in dct:
    values.append(value)

n = len(dct)
for i in range(n):
    for j in range(0, n - i - 1):
        if dct[values[j]] < dct[values[j + 1]]:
            values[j], values[j + 1] = values[j + 1], values[j]

sorted_dict = {}
for value in values:
    sorted_dict[value] = dct[value]
print(sorted_dict)

# Write a program to reverse a dictionary.
dct = {"z": 30, "x": 40, "y": 84, "u": 5}
dct1 = {}
key = list(dct.keys())
for i in range(len(key) - 1, -1, -1):
    dct1[key[i]] = dct[key[i]]
print(dct1)
