# Write a program to find the number of occurrences of each character in a string.
string = "Harutyun Chobanyan"
dct = {}

for elem in string:
    if elem in dct:
        dct[elem] += 1
    else:
        dct[elem] = 1

print(f"Occurrence of all characters in {string} is :\n " + str(dct))

# Write a program to check if a string contains only letters.
string = "Harutyun"

for char in string:
    if not (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):
        print("String contains numbers and symbols")
        break
else:
    print("String contains only letters")

# Write a program to check if a string contains only numbers.
numbers = "1234567522"

for char in numbers:
    if not (48 <= ord(char) <= 57):
        print("String contains letters and symbols")
        break
else:
    print("String contains only numbers")

# Write a program to check if a string contains only alphanumeric characters.

alpha_num_char = "1234jhhsd_=567522"

for char in alpha_num_char:
    if not (48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):
        print("String contains symbols")
        break
else:
    print("String contains only alphanumeric characters")

# Write a program to count the number of vowels in a string.
string = input("Enter string:")
vowels_ctr = 0
for char in string:
    if char in "AEIOUaeiou":
        vowels_ctr += 1
print(vowels_ctr)

# Write a program to count the number of consonants in a string.
string = input("Enter string:")
consonant_ctr = 0
for char in string:
    if char not in "AEIOUaeiou":
        consonant_ctr += 1
print(consonant_ctr)

# Write a program to count the number of words in a string.
string = input("Enter string:")
words_ctr = 0
for char in string:
    if char == " ":
        words_ctr += 1
words_ctr += 1
print(words_ctr)
