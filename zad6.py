def fibonacci_array(n):
    a = 0
    b = 1
    for _ in range(n):
        b = a + b
        a = b-a
        yield a


def main():

    how_much_numbers = 11
    values = fibonacci_array(how_much_numbers)

    for _ in range(how_much_numbers):
        print(next(values))

    # for x in fibonacci_array(how_much_numbers):
    #     print(x)


if __name__ == "__main__":
    main()
