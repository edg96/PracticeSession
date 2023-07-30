import random


def exercise_1() -> set[str]:
    """
    Given the lists:
    employees = ['Maria', 'Marius', 'Andrei', 'Bianca', 'Bogdan', 'Ana', 'Mihai']
    fuel_card = ['Maria', 'Andrei']
    gym_membership = ['Maria', 'Andrei', 'Mihai']

    Which employees have both a fuel card and a gym membership?
    Which employees do not have a fuel card and do not have a gym membership?

    Returns:
        set[str]: A set of employees who have both a fuel card and a gym membership.
    """
    employees = ['Maria', 'Marius', 'Andrei', 'Bianca', 'Bogdan', 'Ana', 'Mihai']
    fuel_card = ['Maria', 'Andrei']
    gym_membership = ['Maria', 'Andrei', 'Mihai']

    new_employee = set(employee for employee in employees
                       if employee in fuel_card and employee in gym_membership)

    return new_employee


def exercise_2() -> str:
    """
    Remove duplicates within a word entered from the keyboard.

    Returns:
        str: The word with duplicates removed.
    """
    word = input('Enter the word: ')

    word_chars = list(word)
    unique_word_chars = set(word)
    new_word = []

    for char in word_chars:
        if char in unique_word_chars and char not in new_word:
            new_word.append(char)

    return ''.join(new_word)


def exercise_4() -> None:
    """
    Find the next 4-digit number with all distinct digits entered
        from the keyboard.
    """
    number = input('Enter your number: ')
    not_distinct = True

    if number.isdigit():
        number = int(number)
        while not_distinct:
            digits = set(str(number))
            if len(digits) == 4:
                print(f'The number with distinct number is {number}')
                not_distinct = False
            else:
                number += 1
    else:
        print('Not a number')


def exercise_5() -> None:
    """
    Print the set of consonants in a text entered from the keyboard.
    """
    text = input('Enter your text: ')

    consonants = set(char for char in text.lower() if char not in ['a', 'e', 'i', 'o', 'u', ' '])

    print(consonants)


def exercise_6() -> None:
    """
    Generate two lists of random numbers and print the common numbers
        and different numbers between them.
    """
    first_list = random.sample(range(0, 25), 10)
    second_list = random.sample(range(0, 25), 10)

    common_numbers = [number for number in first_list if number in second_list]
    different_numbers = [number for number in first_list if number not in second_list]

    print(f'First list: {first_list}')
    print(f'Second list: {second_list}')
    print(f'Common numbers: {common_numbers}')
    print(f'Different numbers: {different_numbers}')


def exercise_7() -> None:
    """
    Generate a list of perfect squares less than 100 and print it.
    """
    perfect_squares = [number**2 for number in range(0, 101) if number**2 < 100]
    print(perfect_squares)


def exercise_8() -> None:
    """
    Convert all numbers in a list to strings and print the updated list.
    """
    numbers = [50, 9, 100, 3, 33, '22']

    numbers_as_strings = [str(number) if isinstance(number, int) else number for number in numbers]
    print(numbers_as_strings)


def exercise_9() -> tuple[dict[str, int], dict[str, int]]:
    """
    Convert the prices of cars to Romanian Lei (RON) and filter the
    cars with prices less than 20000.
    Return two dictionaries: one with cars and their prices in RON,
    and one with cheaper cars.

    Returns:
        tuple[dict[str, int], dict[str, int]]: A tuple containing two dictionaries:
            cars in RON and cheaper cars.
    """
    cars = {
        'Dacia': 15000,
        'Toyota': 20000,
        'BMW': 50000,
        'Audi': 45000,
        'Hyundai': 16500,
        'Mercedes': 70000
    }

    cars_in_ron = {car: price * 5 for car, price in cars.items()}
    cars_lesser_price = {car: price for car, price in cars.items() if price < 20000}

    return cars_in_ron, cars_lesser_price


def exercise_10() -> dict[str, int]:
    """
    Count the occurrence of each character (excluding spaces) in a text
    entered from the keyboard.

    Returns:
        dict[str, int]: A dictionary with each character and its frequency of occurrence.
    """
    text = input('Enter your text: ')

    text_without_spaces = text.replace(' ', '')
    character_occurrence = {letter: text.count(letter) for letter in text_without_spaces}

    return character_occurrence


def exercise_11() -> list[bool]:
    """
    Check if each element in a list is a string and return a list of
        corresponding boolean values.

    Returns:
        list[bool]: A list of boolean values indicating whether each element is
            a string or not.
    """
    datas = [1, 2, 3, 'Python', 'java']

    result = [True if isinstance(element, str) else False for element in datas]

    return result


def exercise_12() -> dict[int, bool]:
    """
    Check if each number in a list is greater than 10 and return a
        dictionary with the numbers as keys and corresponding boolean values
        indicating if they are greater than 10.

    Returns:
        dict[int, bool]: A dictionary with numbers as keys and boolean values indicating
            if they are greater than 10.
    """
    numbers = [1, 2, 3, 100, 200, 300]

    result = {number: (True if number > 10 else False) for number in numbers}

    return result


if __name__ == "__main__":
    pass
