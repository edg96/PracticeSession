def read_names_from_txt(file_path: str) -> list:
    """
    Read names from a text file.

    Parameters:
        file_path (str): The path to the text file containing names.

    Returns:
        list: A list of names read from the text file.
    """
    with open(file_path, 'r') as txt_file:
        names = txt_file.read().split()

    return names


def count_unique_names(names: list[str]) -> dict[str, int]:
    """
    Count the frequency of unique names in a list.

    Parameters:
        names (list[str]): A list of names.

    Returns:
        dict[str, int]: A dictionary where keys are unique names and values are their frequencies.
    """
    unique_names = list(set(names))
    unique_names.sort()
    unique_names_frequency = {name: names.count(name) for name in unique_names}

    return unique_names_frequency


def write_names_to_txt(file_path: str, unique_names_frequency: dict[str, int]):
    """
    Write unique names and their frequencies to a text file.

    Parameters:
        file_path (str): The path to the text file where data will be written.
        unique_names_frequency (dict[str, int]): A dictionary with unique names and their frequencies.
    """
    with open(file_path, 'w') as txt_file:
        content = ''
        for unique_name, frequency in unique_names_frequency.items():
            content += unique_name + ': ' + str(frequency) + '\n'

    txt_file.write(content)


def exercise_1(file_path: str):
    """
    This function reads names from a text file, counts the frequency of unique names,
       and writes the unique names and their frequencies back to the same text file.

    Parameters:
        file_path (str): The path to the text file.
    """
    names = read_names_from_txt(file_path)
    unique_names_frequency = count_unique_names(names)
    write_names_to_txt(file_path, unique_names_frequency)


if __name__ == '__main__':
    pass
