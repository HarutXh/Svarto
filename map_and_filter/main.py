from functions import (
    pos_num_in_str,
    is_even,
    is_odd,
    vowels,
    is_negative,
    is_below_8000,
    add_2000,
)

if __name__ == "__main__":
    string = "I was born on September 6, 2001"
    result = filter(pos_num_in_str, string)
    print(list(result))

    tpl = (1, 2, 3, 4, 5, 6)
    is_even = filter(is_even, tpl)
    is_odd = filter(is_odd, tpl)
    print(list(is_even))
    print(list(is_odd))

    string = "I love Svarto"
    result = filter(vowels, string)
    filtered_vowels_in_string = ""
    for symbol in result:
        filtered_vowels_in_string += symbol
    print(filtered_vowels_in_string)

    numbers = (-2, 5, 8, -23, -4)
    result = filter(is_negative, numbers)
    print(list(result))

    lst = [200, 100, 5000, 14000, 8500, 10000, 400]
    filter_list = filter(is_below_8000, lst)
    map_list = map(add_2000, filter_list)
    print(list(map_list))
