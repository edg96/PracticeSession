import math
import re


def exercise_1(num1: int, num2: int) -> int | None:
    """
    Returns the difference of two numbers if one condition is true, else None.

    :param num1: A natural number (a).
    :param num2: A natural number (b).
    :return: The difference of the two numbers if one condition is true, else None.
    """
    if num1 > num2:
        return num1 - num2
    if num2 > num1:
        return num2 - num1

    return None


def exercise_2(number: int) -> int | str:
    """
    Checks if a 3-digit number is even or odd and returns a specific output based on the parity.

    :param number: A natural number.
    :return: If even, returns the sum of the number and its last digit. If odd, checks if it is a multiple of 3.

    """
    if number % 2 == 0:
        sum_of_digits = number + number % 10
        return sum_of_digits
    if number % 3 == 0:
        return f'{number} is a multiple of 3'
    else:
        return f'{number} is not a multiple of 3'


def exercise_3(username: str, password: str) -> dict:
    """
    Checks username and password. If correct, proceeds to collect user details and
        determines the programmer status.

    :param username: The username of the user.
    :param password: The password of the user.
    :return: The person details as a dictionary.
    """
    correct_username = 'windows_user’'
    correct_password = 'P@rolla'
    person_details = {'First Name': 'N/A', 'Last Name': 'N/A', 'Email': 'N/A', 'IT Status': 'N/A'}
    it_experience = -1

    if username != correct_username:
        print('Wrong username. Access denied!')
    elif password != correct_password:
        print('Wrong password. Access denied!')
    else:
        print('You logged in successfully!')
        person_details['First Name'] = input('Enter your first name: ')
        person_details['Last Name'] = input('Enter your last name: ')
        person_details['Email'] = input('Enter your email: ')
        it_experience = input('Enter your IT experience in years: ')

    if it_experience > 3:
        person_details['IT Status'] = 'Senior'
    elif it_experience > 1:
        person_details['IT Status'] = 'Intermediate'
    elif it_experience > 0:
        person_details['IT Status'] = 'Junior'

    return person_details


def exercise_4(file_full_name: str) -> str:
    """
    Returns the extension of a file name.

    :param file_full_name: The full file name with the extension (sea_picture_20230422.jpg).
    :return: The file extension (.txt, .jpg, .pdf).

    """
    extension_name = file_full_name[file_full_name.rfind('.'):]

    return extension_name


def exercise_5(sentence: str) -> int:
    """
    Returns the number of words in a sentence.

    :param sentence: A sentence to be checked (should have at least 2 words).
    :return: The number of words in the sentence.
    """
    number_of_words = 1
    for element in sentence:
        if element == ' ':
            number_of_words += 1

    return number_of_words


def exercise_6(current_time: int) -> str:
    """
    Determines the color of a traffic light based on the current time.

    :param current_time: The time to be checked in minutes (e.g., 1 hour and 27 minutes -> value should be 87).
    :return: The color of the traffic light.
    """
    last_digit = current_time % 10

    if last_digit in (0, 1, 2, 3, 6, 7, 8):
        return 'It\'s green!'
    return 'It\'s red!'


def exercise_7() -> str:
    """
    Searches for the username from a given string and returns it.

    :return: The username.
    """
    text = 'platform: Solaris; version: 2.5; username: mcristi; all rights reserved to …'
    index_username = text.find('username: ')
    index_seperator = text.rfind(';')
    username = text[index_username + len('username: '):index_seperator]

    return username


def exercise_8(mystery_variable: int | str) -> int | str:
    """
    Raises the mystery_variable to the power of 2 if it's a number or
        returns the mystery_variable if it's a string.

    :param mystery_variable: A mystery value to be evaluated.
    :return: A value or a text depending on the condition met.
    """
    if mystery_variable.isdigit():
        mystery_variable_raised = pow(mystery_variable, 2)
        return mystery_variable_raised
    return mystery_variable


def exercise_9(sentence: str) -> int | str:
    """
    Returns the number of spaces in a string. If there are no spaces, displays a message.

    :param sentence: A sentence to be checked.
    :return: The number of spaces or a message depending on the condition met.
    """
    number_of_spaces = 0

    for letter in sentence:
        if letter == ' ':
            number_of_spaces += 1

    if number_of_spaces > 0:
        return number_of_spaces
    return 'There are not spaces in your string'


def exercise_10(number: str) -> int:
    """
    Calculates the sum of all digits in a number and checks if the sum is divisible by 8.

    :param number: A natural number to be checked.
    :return: The sum of all digits of the number.
    """
    digits = number.split()
    sum_of_number_elements = sum(digits)

    print(f'{number} is ', end='')
    if sum_of_number_elements % 8 != 0:
        print('not ', end='')
    print('divisible by 8.')

    return sum_of_number_elements


def exercise_11(email_address: str) -> str | None:
    """
    Extracts the domain of an email (gmail.com or yahoo.com).

    :param email_address: The email address to be checked.
    :return: The domain of the email or None if it is invalid.
    """
    rgx_email_pattern = r'^[a-zA-Z0-9_.-]+@(gmail|yahoo)\.com$'
    match = re.match(rgx_email_pattern, email_address)

    if match:
        return email_address[email_address.rfind('@')::]
    else:
        return 'Invalid email'


def exercise_12(sentence: str) -> int:
    """
    Calculates the number of vowels in a sentence.

    :param sentence: A sentence to be checked (can be just a word).
    :return: The number of vowels.
    """
    sentence = sentence.lower()
    number_of_vowels = 0

    for char in sentence:
        if char in ('a', 'e', 'i', 'o', 'u'):
            number_of_vowels += 1

    return number_of_vowels


def exercise_13(text_to_convert: str) -> float | str:
    """
    Tries to convert a text into a float. If it is not possible, displays a message.

    :param text_to_convert: A text to be converted.
    :return: The float value or the string message depending on whether it can be converted or not.
    """
    rgx_email_pattern = r'^[1-9]\d*(\.\d+)?$'
    match = re.match(rgx_email_pattern, text_to_convert)

    if match:
        return float(text_to_convert)
    else:
        return 'Cannot convert text. Invalid format'


def exercise_14(number: int) -> int | str:
    """
    Produces a specific output depending on the value comparison to the fixed value 100.

    :param number: A number to be checked.
    :return: The sum of 100 and the number digits or the string 'Python'.
    """
    number = int(number)
    if number > 100:
        sum_of_digits = 0
        while number > 0:
            sum_of_digits += (number % 10)
            number = math.floor(number / 10)
        return sum_of_digits
    else:
        return 'Python'


def exercise_15(sentence: str) -> bool:
    """
    Checks if a sentence starts with the characters 'Python'.

    :param sentence: A sentence to be checked.
    :return: True if the sentence starts with 'Python', False otherwise.
    """
    return sentence.startswith('Python')


if __name__ == "__main__":
    pass
