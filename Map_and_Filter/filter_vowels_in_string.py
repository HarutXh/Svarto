def vowels(char):
    return char in "aeiouAEIOU"


string = "I love Svarto"
result = filter(vowels, string)
filtered_vowels_in_string = ""
for symbol in result:
    filtered_vowels_in_string += symbol
print(filtered_vowels_in_string)
