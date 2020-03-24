from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        print(
            f"Aktualna ilość wywołań funcji: {my_function.__name__} to: {my_function.counter}")
        return func(*args, **kwargs)
    return wrapper


@decorator
def my_function():
    my_function.counter += 1
    print("do something...")


def main():
    my_function.counter = 1
    my_function()
    my_function()
    my_function()


if __name__ == "__main__":
    main()
