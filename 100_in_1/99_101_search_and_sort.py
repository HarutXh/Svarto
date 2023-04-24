# # Write a program to implement the linear search algorithm for a list of integers.
# def linear_search(el, lst):
#     for i in range(len(lst)):
#         if lst[i] == el:
#             return f"index of {el} is {i}"
#     return -1


# lst = [5, 15, 85, 477]
# el = int(input("Enter element: "))
# print(linear_search(el, lst))

# # Write a program to implement the merge sort algorithm for a list of integers.
# def merge_sort(lst):
#     if len(lst) > 1:
#         mid = len(lst) // 2
#         left_half = lst[:mid]
#         right_half = lst[mid:]
#         merge_sort(left_half)
#         merge_sort(right_half)
#         i = j = k = 0
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 lst[k] = left_half[i]
#                 i += 1
#             else:
#                 lst[k] = right_half[j]
#                 j += 1
#             k += 1
#         while i < len(left_half):
#             lst[k] = left_half[i]
#             i += 1
#             k += 1
#         while j < len(right_half):
#             lst[k] = right_half[j]
#             j += 1
#             k += 1
#     return lst


# lst = [6, 8, 4, 7, 2]
# print(merge_sort(lst))

# # Write a program to implement the quicksort algorithm for a list of integers.
# # pivot middle element
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]

#     return quick_sort(left) + middle + quick_sort(right)


# arr = [4, 8, 6, 3, 2, 9]
# print(quick_sort(arr))


# # pivot last_element
# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1

#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1


# def quick_sort(arr, low, high):
#     if low < high:
#         pivot_index = partition(arr, low, high)
#         quick_sort(arr, low, pivot_index - 1)
#         quick_sort(arr, pivot_index + 1, high)


# arr = [3, 1, 4, 2, 5]
# quick_sort(arr, 0, len(arr) - 1)
# print(arr)


# # pivot first element
# def partition(arr, low, high):
#     pivot = arr[low]
#     i = low + 1
#     j = high

#     while True:
#         while i <= j and arr[i] <= pivot:
#             i += 1
#         while i <= j and arr[j] >= pivot:
#             j -= 1
#         if i <= j:
#             arr[i], arr[j] = arr[j], arr[i]
#         else:
#             break

#     arr[low], arr[j] = arr[j], arr[low]
#     return j


# def quick_sort(arr, low, high):
#     if low < high:
#         pivot_index = partition(arr, low, high)
#         quick_sort(arr, low, pivot_index - 1)
#         quick_sort(arr, pivot_index + 1, high)


# arr = [3, 1, 4, 2, 5]
# quick_sort(arr, 0, len(arr) - 1)
# print(arr)
