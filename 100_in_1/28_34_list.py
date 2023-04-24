# # Write a program to find the sum of all the elements in a list.
# lst = []
# length = int(input("Enter length:"))
# for i in range(length):
#     element = int(input("Enter element:"))
#     lst.append(element)
# sum = 0
# for i in range(len(lst)):
#     sum += lst[i]
# print(sum)

# # Write a program to find the product of all the elements in a list.
# lst = []
# length = int(input("Enter length:"))
# for i in range(length):
#     element = int(input("Enter element:"))
#     lst.append(element)
# mult = 1
# for i in range(len(lst)):
#     mult *= lst[i]
# print(mult)

# # Write a program to find the largest element in a list.
# lst = []
# length = int(input("Enter length: "))
# for i in range(length):
#     element = int(input("Enter element: "))
#     lst.append(element)
# max = lst[0]
# for i in lst:
#     if i > max:
#         max = i
# print(max)

# # Write a program to find the smallest element in a list.
# lst = []
# length = int(input("Enter length: "))
# for i in range(length):
#     element = int(input("Enter element: "))
#     lst.append(element)
# min = lst[0]
# for i in lst:
#     if i < min:
#         min = i
# print(min)

# # Write a program to sort a list in ascending order.
# lst = []
# length = int(input("Enter length: "))
# for i in range(length):
#     element = int(input("Enter element: "))
#     lst.append(element)
# min = lst[0]
# for i in range(length):
#     for j in range(length):
#         if lst[i] < lst[j]:
#             temp = lst[i]
#             lst[i] = lst[j]
#             lst[j] = temp
# print(lst)

# # Write a program to sort a list in descending order.
# lst = []
# length = int(input("Enter length: "))
# for i in range(length):
#     element = int(input("Enter element: "))
#     lst.append(element)
# min = lst[0]
# for i in range(length):
#     for j in range(length):
#         if lst[i] > lst[j]:
#             temp = lst[i]
#             lst[i] = lst[j]
#             lst[j] = temp
# print(lst)

# Write a program to reverse a list.
# lst = []
# length = int(input("Enter length: "))
# for i in range(length):
#     element = int(input("Enter element: "))
#     lst.append(element)
# print(lst[::-1])
