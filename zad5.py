def primes_cmplist(my_list):

    # result = [el for el in my_list if all(el % x != 0 for x in range(2, el))]
    result = [number**2 for number in my_list if test_prime(number)]
    return result


def primes_filter_map(my_list):
    result = list(map(lambda number: number**2, filter(test_prime, my_list)))
    return result


def test_prime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2, n):
            if(n % x == 0):
                return False
        return True


def main():

    how_much_numbers = 100
    list_with_defined_range = list(range(2, how_much_numbers))

    print(

        f"""  \nCiąg liczb pierwszych poniesionych do kwadratu w podanym zakresie
wygenerowany za pomocją comperhention list:
{primes_cmplist(list_with_defined_range)}""")

    print(

        f"""  \nCiąg liczb pierwszych poniesionych do kwadratu w podanym zakresie
wygenerowany za pomocją funkcji map() i filter():
{primes_filter_map(list_with_defined_range)}""")


if __name__ == "__main__":
    main()
