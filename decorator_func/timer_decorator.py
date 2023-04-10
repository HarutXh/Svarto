import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Function {func.__name__} took {end_time - start_time:.6f} seconds to execute."
        )
        return result

    return wrapper


@timer_decorator
def my_function():
    total = 0
    for i in range(10000000):
        total += i
    return total


if __name__ == "__main__":
    my_function()
