def memoize(func):
    cache = {}

    def memo_func(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return memo_func


@memoize
def my_func(a, b):
    return a + b


if __name__ == "__main__":
    print(my_func(5, 4))
