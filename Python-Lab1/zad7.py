from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(
            f"Jestem dekoratorem: Parametry funkcji {my_function.__name__} to {args}")
        return func(*args, **kwargs)
    return wrapper


@decorator
def my_function(arg1, arg2):
    print(
        f"Sprawdzam dekorator: Jestem funckją {my_function.__name__} moje argumenty to: {arg1, arg2}")


def main():
    my_function("a", "b")


if __name__ == "__main__":
    main()
