def exercise_1() -> tuple[str, str]:
    """
    Answers a question about list comparison and identity.

    :return: Two strings explaining the expected output of the code.
    """
    print('The following lists are defined:')
    print('lst_1 = [1, 2, 3, 4]')
    print('lst_2 = [1, 2, 3, 4]')
    print('print(lst_1 == lst_2, lst_1 is lst_2)')
    print('What is printed?')
    print('a. True True')
    print('b. True False')
    print('c. False True')
    print('d. False False')
    print('Why did you make this choice?')

    return '1. True: because the values are equal.', '1. False: because the memory address is different.'


def exercise_2(datas: list) -> int | float:
    """
    Displays the largest number in a list that can contain any type of data.

    :param datas: A list that can contain any type of data.
    :return: The biggest number in the list.
    """
    number = []

    for element in datas:
        if isinstance(element, int) or isinstance(element, float):
            number.append(element)

    return max(number)


def exercise_3(sentence: str) -> str:
    """
    Removes all the words that start with 'A'/'a' from a sentence.

    :param sentence: A sentence to be checked (can contain any words).
    :return: The sentence without the words starting with 'A'/'a'.
    """
    all_words = sentence.split()
    words_not_starting_with_a = []

    for word in all_words:
        if not word.startswith(('A', 'a')):
            words_not_starting_with_a.append(word)

    new_text = ' '.join(words_not_starting_with_a)

    return new_text


def exercise_4(list1: list[int | float], list2: list[int | float]) -> int | float:
    """
    Calculates the sum of the two smallest positive numbers in
        two lists (which can contain negative values).

    :param list1: A list that can contain numbers (positive or negative).
    :param list2: A list that can contain numbers (positive or negative).
    :return: The sum according to the condition.
    """
    min_positive_first_list = min(list1)
    min_positive_second_list = min(list2)

    sum_of_min_values = min_positive_first_list + min_positive_second_list

    return sum_of_min_values


def exercise_5(number: int) -> int:
    """
    Displays the next 4-digit number with all distinct digits.

    :param number: A number to be checked.
    :return: The next number with distinct digits.
    """
    not_distinct = True
    number = int(number)

    while not_distinct:
        digits = set(str(number))
        if len(digits) == 4:
            return number
        else:
            number += 1


def exercise_6(words: list[str]) -> str:
    """
    Finds the longest common prefix among a list of words.

    :param words: A list of words (should contain at least 2).
    :return: The longest common prefix as a string.
    """
    shortest_word = min(words)
    list_of_letters_prefix = []

    for i in range(0, len(shortest_word)):
        if words[0][i] == words[1][i] == words[2][i]:
            list_of_letters_prefix.append(words[0][i])
        else:
            break

    common_sequence = ''.join(list_of_letters_prefix)

    return common_sequence


def exercise_7(words: list[str]) -> list[str]:
    """
    Displays a list where the words from the original list
        are written in reverse (from right to left).

    :param words: A list of words (should contain at least 2 words).
    :return: A list of reversed words.
    """
    new_words = []

    for word in words:
        split_word = list(word)
        split_word.reverse()
        new_words.append(''.join(split_word))

    return new_words


def exercise_8(words: list[str]) -> list[str]:
    """
    Displays the words that have a number of characters greater than
        the average character count in a list of words.

    :param words: A list of words.
    :return: A list of words that meet the given condition.
    """
    total_numbers_length = 0

    for element in words:
        total_numbers_length += len(element)

    words_arithmetic_length = round(total_numbers_length / len(words))
    new_word_list = [element for element in words if len(element) > words_arithmetic_length]

    return new_word_list


def exercise_9(word: str) -> str:
    """
    Replaces the character '-' with the character '_'.

    :param word: The word to have its specific characters replaced.
    :return: The replaced word.
    """
    new_word = word.replace('-', '_')

    return new_word


if __name__ == "__main__":
    pass
