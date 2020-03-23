def words_count(path):
    number_of_words = 0
    with open(path) as fd:

        for line in fd:
            words = line.split()
            for i in words:
                number_of_words += 1
    return (number_of_words)


def words_count_with_len(path):
    number_of_words = 0
    with open(path) as fd:

        for line in fd:
            words = line.split()
            number_of_words += len(words)
    return(number_of_words)


def main():
    path = "Lab1_Pyth\\test1.txt"
    print(f"ilość słów w pliku to: {words_count(path)}")
    print(f"ilość słów w pliku to: {words_count_with_len(path)}")


if __name__ == "__main__":
    main()
