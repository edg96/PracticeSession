import random
import re


def exercise_1() -> list[int]:
    """
    Displays all even numbers between 0 and 3000.

    :return: A list of even numbers between the fixed interval.
    """
    even_numbers = [number for number in range(0, 3001, 2)]

    return even_numbers


def exercise_2() -> list[int]:
    """
    Displays all prime numbers between 0 and 1000.

    :return: A list of prime numbers between the fixed interval.
    """
    prime_numbers = [i for i in range(2, 1001) if all(i % j != 0 for j in range(2, round(i/2)))]

    return prime_numbers


def exercise_3() -> str:
    """
    Prompts the user to guess a number randomly chosen by the program.
    Gives hints after each guess to help the user know if they need to go higher or lower.

    :return: A message indicating that the user guessed the number.
    """
    number = random.randint(1, 100)
    guess = -1

    while guess != number:
        guess = int(input('Insert your guess: '))
        if guess < number:
            print('You need to go higher.')
        elif guess > number:
            print('You need to go lower.')
        else:
            return 'You guessed the number.'


def exercise_4() -> str:
    """
    Creates a menu where the user can fill different information.

    :return: A goodbye message.
    """
    while True:
        print('Press 1 to enter the username.')
        print('Press 2 to enter the password.')
        print('Press 3 to enter the email.')
        print('Press 4 to enter the details (user, password, email).')
        print('Press E/e to exit the program')
        choice = input('Enter between 1,2,3,4 or E/e: ')
        choice = choice.lower()

        if choice == '1':
            username = input('Enter the username: ')
            print(f'You inserted the username: {username}\n')
        elif choice == '2':
            password = input('Enter the password: ')
            print(f'You inserted the password: {password}\n')
        elif choice == '3':
            email = input('Enter the email: ')
            print(f'You inserted the email: {email}\n')
        elif choice == '4':
            username = input('Enter the username: ')
            print(f'You inserted the username: {username}')
            password = input('Enter the password: ')
            print(f'You inserted the password: {password}')
            email = input('Enter the email: ')
            print(f'You inserted the email: {email}\n')
        elif choice == 'e':
            return 'Exiting the menu. Goodbye!'
        else:
            print('Invalid choice. Please try again.')


def exercise_5(sentence: str) -> tuple[int, int]:
    """
    Calculates the number of vowels and consonants in a sentence.

    :param sentence: A sentence to be checked.
    :return: The number of vowels and consonants.
    """
    sentence = sentence.lower()
    number_of_vowels, number_of_consonants = 0, 0

    for element in sentence:
        if element == ' ':
            continue
        else:
            if element in ('a', 'e', 'i', 'o', 'u'):
                number_of_vowels += 1
            else:
                number_of_consonants += 1

    return number_of_vowels, number_of_consonants


def exercise_6(text1: str, text2: str) -> dict:
    """
    Determines the number of common characters from two strings.

    :param text1: The first text.
    :param text2: The second text.
    :return: A dictionary with the number of common characters and the list of common characters.
    """
    number_of_common_characters = 0
    list_of_common_characters = []

    set_of_text1 = set(text1)
    set_of_text2 = set(text2)

    for element in set_of_text1:
        if element in set_of_text2:
            number_of_common_characters += 1
            list_of_common_characters.append(element)

    return {number_of_common_characters: list_of_common_characters}


def exercise_7(number: int) -> int:
    """
    Calculates the Fibonacci of a number.

    :param number: A natural number to be checked.
    :return: The Fibonacci number.
    """
    product = 1
    for i in range(1, number+1):
        product *= i

    return product


def exercise_8(gmail_address: str) -> bool:
    """
    Validates a GMail address with the following rules:
    - It must end with '@gmail.com'.
    - It must be in the form 'name@gmail.com'.
    - The name must not contain special characters: (+=~!@#$%^&*()[]{}\’”;,/”)

    :param gmail_address: An email address (GMail only).
    :return: True if the GMail address is valid, False otherwise.
    """
    rgx_email_pattern = r'^(?!.*[+=~!@#$%^&*()\[\]{}\’”;,/])[a-zA-Z0-9._]+@gmail\.com$'
    match = re.match(rgx_email_pattern, gmail_address)

    if match:
        return True
    return False


def exercise_9(sentence: str) -> bool:
    """
    Checks if a sentence has only distinct characters.

    :param sentence: A sentence to be checked.
    :return: True if the sentence has only distinct characters, False otherwise.
    """
    sentence.replace(' ','')

    if len(set(sentence)) == len(list(sentence)):
        return True
    return False


def exercise_10(sentence: str) -> dict:
    """
    Counts the number of letters, digits, symbols, and spaces within a sentence.

    :param sentence: A sentence (can contain any category of characters).
    :return: A dictionary with each category and its corresponding number of occurrences.
    """
    set_of_character = {'Chars': 0, 'Digits': 0, 'Symbols': 0, 'Spaces': 0}

    for element in sentence:
        if element.isalpha():
            set_of_character['Chars'] += 1
        elif element.isdigit():
            set_of_character['Digits'] += 1
        elif element.isspace():
            set_of_character['Spaces'] += 1
        else:
            set_of_character['Symbols'] += 1

    return set_of_character


if __name__ == "__main__":
    pass
