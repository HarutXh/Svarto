# Write a program to find the length of a string.
string = input("Enter string: ")
print(len(string))

# Write a program to concatenate two strings.
string1 = input("Enter string 1: ")
string2 = input("Enter string 2: ")
print(string1 + string2)

# Write a program to find the substring of a string.
string = input("Enter string: ")
string += " "
word = input("Enter word: ")
word_in_text = ""
for symbol in string:
    if symbol != " ":
        word_in_text += symbol
    else:
        if word == word_in_text:
            print("Found")
            break
        else:
            word_in_text = ""
else:
    print("Not Found")


# Write a program to find the index of a substring in a string.
def find_substring(string, substring):
    index = -1
    n = len(string)
    m = len(substring)

    for i in range(n - m + 1):
        if string[i : i + m] == substring:
            index = i
            break

    return index


string = "hello world"
substring = "world"
index = find_substring(string, substring)
print(index)

# Write a program to replace a substring in a string with another substring.
string = "hello world"
old_substring = "world"
new_substring = "python"

index = -1
for i in range(len(string)):
    if string[i : i + len(old_substring)] == old_substring:
        index = i
        break

if index != -1:
    new_string = string[:index] + new_substring + string[index + len(old_substring) :]
else:
    new_string = string

print(new_string)

# Write a program to count the number of occurrences of a substring in a string.
string = "Harutyun"
substring = "u"

count = 0
for i in range(len(string) - len(substring) + 1):
    if string[i : i + len(substring)] == substring:
        count += 1

print(count)

# Write a program to convert a string to uppercase.
string = input("Enter string:")
upper_string = ""

for symbol in string:
    symbol_to_num = ord(symbol)
    if symbol_to_num >= 97 and symbol_to_num <= 122:
        upper_string += chr((symbol_to_num - 32))
    else:
        upper_string += symbol
print("The Result of them =", upper_string)

# Write a program to convert a string to lowercase.
string = input("Enter string:")
lower_string = ""

for symbol in string:
    symbol_to_num = ord(symbol)
    if symbol_to_num >= 65 and symbol_to_num <= 97:
        lower_string += chr((symbol_to_num + 32))
    else:
        lower_string += symbol
print("The Result of them =", lower_string)

# Write a program to remove all whitespace from a string.
string = input("Enter string:")
new_string = ""
for symbol in string:
    if symbol != " ":
        new_string += symbol
print(new_string)

# Write a program to split a string into a list.
string = "Harutyun"
lst = []

for symbol in string:
    lst.append(symbol)

print(lst)

# Write a program to join a list into a string.
lst = ["How", "are", "you", "?"]
string = ""

for x in lst:
    string += x + " "

print(string)

# Write a program to check if a string is a palindrome.
string = input("Please enter your own : ")

for i in range(len(string) // 2):
    if string[i] != string[len(string) - i - 1]:
        print("This is not polindrome")
        break
else:
    print("This is polindrome")
