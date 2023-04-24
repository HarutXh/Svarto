# Write a program to find the sum of all the even numbers in a list.
lst = []
length = int(input("Enter length:"))
for i in range(length):
    element = int(input("Enter element:"))
    lst.append(element)
sum = 0
for i in range(len(lst)):
    if lst[i] % 2 == 0:
        sum += lst[i]
print(sum)

# Write a program to find the sum of all the odd numbers in a list.
lst = []
length = int(input("Enter length:"))
for i in range(length):
    element = int(input("Enter element:"))
    lst.append(element)
sum = 0
for i in range(len(lst)):
    if lst[i] % 2 == 1:
        sum += lst[i]
print(sum)

# Write a program to find the average of a list of numbers.
lst = []
length = int(input("Enter length:"))
for i in range(length):
    element = int(input("Enter element:"))
    lst.append(element)
sum = 0
index = 0
for i in range(len(lst)):
    sum += lst[i]
    index = len(lst)
    average = sum / index
print(average)

# Write a program to remove duplicates from a list.
lst = []
length = int(input("Enter length:"))
for i in range(length):
    element = int(input("Enter element:"))
    lst.append(element)
print(lst)
not_duplicate_lst = []
for num in lst:
    if num not in not_duplicate_lst:
        not_duplicate_lst.append(num)
print(not_duplicate_lst)

# Write a program to find the second largest number in a list.
lst = []
length = int(input("Enter length:"))
for i in range(length):
    element = int(input("Enter element:"))
    lst.append(element)
max_num = 0
second_max = 1
for num in lst:
    if num > max_num:
        second_max = max_num
        max_num = num
    elif num > second_max and num != max_num:
        second_max = num
print("The second largest number in the list is:", second_max)

# Write a program to find the second smallest number in a list.
lst = []
length = int(input("Enter length:"))
for i in range(length):
    element = int(input("Enter element:"))
    lst.append(element)
min_num = lst[0]
second_min = len(lst)
for num in lst:
    if num < min_num:
        second_min = min_num
        min_num = num
    elif num < second_min and num != min_num:
        second_min = num
print("The second smallest number in the list is:", second_min)


# Write a program to find the median of a list of numbers.
def find_median(numbers):
    length = len(numbers)
    midpoint = length // 2
    for i in range(midpoint):
        min_idx = i
        for j in range(i + 1, length):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    if length % 2 == 0:
        return (numbers[midpoint - 1] + numbers[midpoint]) / 2
    else:
        return numbers[midpoint]


numbers = [2, 5, 1, 9, 7]
median = find_median(numbers)
print(median)


# Write a program to find the mode of a list of numbers.
def find_mode(numbers):
    frequency = {}
    max_frequency = 0
    mode = 0

    for number in numbers:
        if number not in frequency:
            frequency[number] = 1
        else:
            frequency[number] += 1

        if frequency[number] > max_frequency:
            max_frequency = frequency[number]
            mode = number

    return mode


numbers = [2, 5, 1, 9, 7, 2, 2]
mode = find_mode(numbers)
print(mode)


# Write a program to find the standard deviation of a list of numbers.
def find_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count


def find_standard_deviation(numbers):
    mean = find_mean(numbers)
    squared_differences = [(number - mean) ** 2 for number in numbers]
    variance = sum(squared_differences) / len(numbers)
    standard_deviation = (variance) ** 0.5
    return standard_deviation


numbers = [2, 5, 1, 9, 7]
std_deviation = find_standard_deviation(numbers)
print(std_deviation)


# Write a program to find the variance of a list of numbers.
def find_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count


def find_variance(numbers):
    mean = find_mean(numbers)
    squared_differences = [(number - mean) ** 2 for number in numbers]
    variance = sum(squared_differences) / len(numbers)
    return variance


numbers = [2, 5, 1, 9, 7]
variance = find_variance(numbers)
print(variance)


# Write a program to convert a list of integers to a binary string.
def list_to_binary_string(lst):
    binary_string = ""
    for num in lst:
        binary = bin(num)[2:]  # convert num to binary and remove the '0b' prefix
        num_zeros_to_pad = 4 - len(binary)
        binary_string += (
            "0" * num_zeros_to_pad + binary
        )  # pad binary with leading zeros
    return binary_string


int_list = [2, 5, 1, 9, 7]
binary_string = list_to_binary_string(int_list)
print(binary_string)


# Write a program to convert a binary string to a list of integers.
def binary_string_to_int_list(binary_string):
    binary_chunks = [binary_string[i : i + 8] for i in range(0, len(binary_string), 8)]
    int_list = [int(chunk, 2) for chunk in binary_chunks]
    return int_list


binary_string = "0100100001100101011011000110110001101111"
int_list = binary_string_to_int_list(binary_string)
print(int_list)
