def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 == 1


tpl = (1, 2, 3, 4, 5, 6)
is_even = filter(is_even, tpl)
is_odd = filter(is_odd, tpl)
print(list(is_even))
print(list(is_odd))
