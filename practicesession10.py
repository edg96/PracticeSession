import time


def add_elements_with_append() -> float:
    """
    Adds elements to a list using the append method in a for loop.

    :return: The time taken to add elements to the list.
    """
    lst = []
    start_time = time.time()
    for i in range(10_000):
        lst.append(i)
    end_time = time.time()
    return end_time - start_time


def add_elements_with_comprehension() -> float:
    """
    Adds elements to a list using list comprehension.

    :return: The time taken to add elements to the list.
    """
    start_time = time.time()
    _ = [i for i in range(10_000)]
    end_time = time.time()
    return end_time - start_time


def exercise_1() -> dict:
    """
    Compares the time taken to add elements to a list using append and list comprehension.

    :return: A dictionary containing the time taken with append and list comprehension.
    """
    time_with_append = add_elements_with_append()
    time_with_comprehension = add_elements_with_comprehension()

    time_comparison = {'Time with append': {time_with_append},
                       'Time with list comprehension': {time_with_comprehension}}

    return time_comparison


def exercise_2(text: str) -> int:
    """
    Finds the numbers in a text and returns their sum.

    :param text: The input string.
    :return: The sum of all numbers found in the text.
    """
    words_and_numbers = text.split()
    numbers = [int(element) for element in words_and_numbers if element.isdigit()]

    return sum(numbers)


def exercise_3(*args: any) -> list:
    """
    Returns a list containing all the elements passed as arguments.

    :param args: Variable number of arguments of any type.
    :return: A list containing all the elements passed as arguments.
    """
    return list(args)


def exercise_4(file_name: str) -> str:
    """
    Returns the file type based on the given file name.

    :param file_name: The name of the file.
    :return: The file type.
    """
    return file_name[file_name.rfind('.')::]


def exercise_5(word: str) -> bool:
    """
    Checks if a word contains unique letters.

    :param word: The input word.
    :return: True if the word contains unique letters, False otherwise.
    """
    return len(word) == len(set(word))


def exercise_6(numbers: int) -> str:
    """
    Converts a number into its decimal representation.

    :param numbers: The input number.
    :return: The decimal representation of the number.
    """
    number_decimals = [int(digit) * 10 ** (len(str(numbers)) - 1 - i)
                       for i, digit in enumerate(str(numbers))
                       if digit != 0]

    return ' + '.join(map(str, number_decimals))


def exercise_7(words: list[str]) -> dict:
    """
    Calculates the score of each word based on the sum of positions of its letters in the alphabet.

    :param words: A list of words.
    :return: A dictionary mapping each word to its score.
    """
    points = {word: sum(ord(letter) for letter in word.lower()) for word in words}

    return points


def exercise_8():
    """
    Sorts the `datas` list by name, age, and height in ascending order.

    :return: None
    """
    data1 = ('Dan', 33, 170)
    data2 = ('Mihai', 20, 180)
    data3 = ('Daniel', 40, 173)
    datas = [data1, data2, data3]

    datas.sort(key=lambda name: name[0])
    print(datas)
    datas.sort(key=lambda age: age[1])
    print(datas)
    datas.sort(key=lambda height: height[2])
    print(datas)


def exercise_9(numbers: list[int]) -> dict:
    """
    Checks each number and associates how many numbers are lesser in value than itself.

    :param numbers: A list of integers.
    :return: A dictionary with each number as the key and the number of values lesser than itself as the value.
    """
    numbers.sort()

    return dict(enumerate(numbers))


def exercise_10(number_of_lines: int):
    """
    Prints a pattern of asterisks in a triangle shape.

    :param number_of_lines: The number of lines in the triangle pattern.
    :return: None
    """
    current_line = 1
    while current_line <= number_of_lines:
        for _ in range(0, current_line * 2 - 1):
            print('*', end='')
        print()
        current_line += 1


def exercise_11(text: str) -> str:
    """
    Removes multiple spaces between words in a string and returns the updated string.

    :param text: The input string.
    :return: The string with multiple spaces between words replaced by a single space.
    """
    return ' '.join(text.split())


if __name__ == "__main__":
    pass
