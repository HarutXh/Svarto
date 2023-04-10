def log_decorator(func):
    def log(*args, **kwargs):
        print(f"Function {func.__name__} called")
        print(f"{func.__name__}'s arguments is {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result

    return log


@log_decorator
def add_numbers(a, b=6):
    return a + b


if __name__ == "__main__":
    add_numbers(a=1, b=2)
