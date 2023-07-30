def exercise_1(employees: list[str], email: list[str]) -> dict[str, str]:
    """
    Associates the email with an employee name.

    Parameters:
        employees (list[str]): A list of employee names.
        email (list[str]): A list of corresponding employee email addresses.

    Returns:
        dict[str, str]: A dictionary with the email (key) and the corresponding
            employee associated with it (value).
    """
    new_structure = {email[index]: employee for index, employee in enumerate(employees)}

    return new_structure


def exercise_2() -> str:
    """
    Extracts the temperature in Celsius in Bucharest plus the sky condition.

    Returns:
        str: A message with the temperature and the sky condition.
    """
    weather_statistics = {
        "coord": {
            "lon": 26.1063,
            "lat": 44.4323
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01n"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 286.87,
            "feels_like": 286.07,
            "temp_min": 284.2,
            "temp_max": 289.74,
            "pressure": 1022,
            "humidity": 68
        },
        "visibility": 10000,
        "wind": {
            "speed": 1.03,
            "deg": 260
        },
        "clouds": {
            "all": 0
        },
        "dt": 1666984646,
        "sys": {
            "type": 2,
            "id": 2037828,
            "country": "RO",
            "sunrise": 1666932421,
            "sunset": 1666969892
        },
        "timezone": 10800,
        "id": 683506,
        "name": "Bucharest",
        "cod": 200
    }

    temperature_and_sky_condition = f'{weather_statistics["name"]}: {weather_statistics["weather"][0]["description"]}'

    return temperature_and_sky_condition


def exercise_3(math_grades: dict[str, int]) -> list[str]:
    """
    Finds the student or students with the highest grade.

    Parameters:
        math_grades (dict[str, int]): A dictionary with student names as keys and
            corresponding grades as values.

    Returns:
        list[str]: A list with one or more students that have the highest grade.
    """
    grades = math_grades.values()
    max_grade = max(grades)

    students_with_max_grade = [student for student in math_grades if math_grades[student] == max_grade]

    return students_with_max_grade


def exercise_4() -> dict[int, dict[str, any]]:
    """
    Allows the user to select an employee and modify their salary.

    Returns:
        dict[int, dict[str, any]]: The dictionary with the updated salary.
    """
    employees = {
        1: {'name': 'Andrei', 'salary': 100},
        2: {'name': 'Vlad', 'salary': 500},
        3: {'name': 'Ioana', 'salary': 330}
    }

    choice = -1
    while choice not in [1, 2, 3]:
        choice = int(input('Select the employee: '))

    new_salary = input('Enter the new salary: ')
    employees[choice]['salary'] = int(new_salary)

    return employees


def exercise_5(numbers: list[int]) -> dict[int, int]:
    """
    Checks the frequency of occurrence of each integer from a given list.

    Parameters:
        numbers (list[int]): A list of integers.

    Returns:
        dict[int, int]: A dictionary with each number (key) and its specific frequency
            of occurrence (value).
    """
    unique_numbers = set(numbers)
    numbers_frequency = {number: numbers.count(number) for number in unique_numbers}

    return numbers_frequency


def exercise_6(info_grades: dict[str, list[int | float]]) -> tuple[dict[str, float], list[str]]:
    """
    Based on the grades of the students, calculates each student's average grade and
    finds the student(s) that have at least 3 grades.

    Parameters:
        info_grades (dict[str, list[int | float]]): A dictionary with student names
            as keys and corresponding lists of grades as values.

    Returns:
        tuple[dict[str, float], list[str]]: A dictionary with each student (key) and their
            average grade (value), and a list with the student(s) that have at least 3
            grades if applicable.
    """
    students_average_grades = {student: round((sum(grades) / len(grades)), 2)
                               for student, grades in info_grades.items()}

    students_with_three_grades = [student for student in info_grades
                                  if len(info_grades[student]) >= 3]

    return students_average_grades, students_with_three_grades


def exercise_7(files: list[str]) -> dict[str, str]:
    """
    Finds the corresponding path of each file based on its extension.

    Parameters:
        files (list[str]): A list of file names.

    Returns:
        dict[str, str]: A dictionary with each file (key) and its corresponding path (value).
    """
    paths = {
        'C://Downloads//Images': ['jpg', 'png', 'jpeg'],
        'C://Downloads//Text': ['txt'],
        'C://Downloads//Python_files': ['py'],
        'C://Downloads//PDF': ['pdf'],
    }

    files_and_extensions = {file: file[file.rfind('.') + 1:]
                            for file in files
                            for path, extension in paths.items()
                            if file[file.rfind('.') + 1:] in extension}

    return files_and_extensions


def exercise_8() -> tuple[dict[str, int], dict[str, str]]:
    """
    Finds the cars that are cheaper than 40000 Euros and
    converts each car price to Romanian Lei (RON).

    Returns:
        tuple[dict[str, int], dict[str, str]]: A dictionary with each car (key) that
            is cheaper than 40000 euros and its price (value),
            and a dictionary with each car (key) and its price converted to Romanian Lei (value).
    """
    cars = {
        'Dacia': 15000,
        'Toyota': 20000,
        'BMW': 50000,
        'Audi': 45000,
        'Hyundai': 16500,
        'Mercedes': 70000
    }

    cheaper_cars = {car: price for car, price in cars.items() if price < 40000}
    cars_in_lei = {car: str(price * 5) + ' RON' for car, price in cars.items()}

    return cheaper_cars, cars_in_lei


if __name__ == "__main__":
    pass
