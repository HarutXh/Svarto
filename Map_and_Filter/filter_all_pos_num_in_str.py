def pos_num_in_str(num):
    if num in "0123456789":
        return True
    else:
        return False


string = "I was born on September 6, 2001"
result = filter(pos_num_in_str, string)
print(list(result))
