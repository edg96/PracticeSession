def exercise_1() -> str:
    """
    Returns the answer to a question about valid variable names.

    :return: The answer to the question.
    """
    print('1. Which of the following is a valid variable name?')
    print('a. my-name')
    print('b. 2ndname')
    print('c. 2nd_name')
    print('d. second_name')
    print('e. All of the above')

    answer = 'd. second_name'

    return answer


def exercise_2() -> str:
    """
    Returns the answer to a question about float numbers.

    :return: The answer to the question.
    """
    print('Which number is not a float?')
    print('a. -33.15')
    print('b. 7')
    print('c. 10.0')
    print('d. 11.3')
    print('e. All of the above')

    answer = 'b. 7'

    return answer


def exercise_3() -> str:
    """
    Returns the answer to a question about code lines that generate errors.

    :return: The answer to the question.
    """
    print('Which lines of code generate errors?')
    print('a. my_name = \'Ionut\' # numele meu')
    print('b. my_name == \'Ionut\'')
    print('c. my-name = 100')
    print('d. 1st_name = \'\'\'Ionut Popescu’’’')
    print('e. print(\'numele meu este: \', my_name)')

    answer = 'c, d -> Invalid syntax on naming the variable'

    return answer


def exercise_4(name: str, age: int) -> str:
    """
    Builds a message with the name and age of the user based on their inputs.

    :param name: The name of the person.
    :param age: The age of the person.
    :return: The message with name and age.
    """
    name_and_age = f'{name} is {age} years old'

    return name_and_age


def exercise_5(weight: int | float, height: int | float) -> str:
    """
    Evaluates user weight status based on the BMI (body mass index)

    :param (int | float) weight: the weight of the person
    :param (int | float) height: the weight of the person
    :return: the weight status of the person as a message
    """
    body_mass_index = float(weight) / pow(float(height), 2)
    if body_mass_index < 18.5:
        weight_status = 'Underweight'
    elif body_mass_index < 24.9:
        weight_status = 'Healthy weight'
    elif body_mass_index < 29.9:
        weight_status = 'Overweight'
    else:
        weight_status = 'Obese'

    return weight_status


def exercise_6(edge1: float, edge2: float) -> tuple[float, float]:
    """
    Calculates the area and perimeter of a right-angled triangle.

    :param edge1: One edge of the triangle.
    :param edge2: The other edge of the triangle.
    :return: A tuple containing the area and perimeter of the triangle.
    """
    area = 0.5 * edge1 * edge2
    perimeter = edge1 + edge2 + (edge1 ** 2 + edge2 ** 2) ** 0.5

    return area, perimeter


if __name__ == "__main__":
    pass
