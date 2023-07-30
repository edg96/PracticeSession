from practicesession9ex1ex2 import *
from practicesession9ex3 import *
from practicesession9ex4 import *


def exercise_1(file_path: str):
    """
    Parameters:
        file_path (str): The file path to the Excel file.

    Note:
        The functions should are defined elsewhere and imported to this module.
    """
    employees_per_manager = get_managers_number_of_employees(file_path)
    print(employees_per_manager)
    employees_manager_pair = get_employees_manager_pair(file_path)
    print(employees_manager_pair)

    salary_in_euros = get_salaries_in_euros(file_path, 'Departament IT')
    salary_in_ron = salary_euros_to_ron(salary_in_euros)
    create_ron_converted_column(file_path, 'Departament IT', 6, 'Salariu Lunar [RON]', salary_in_ron)

    salary_in_euros = get_salaries_in_euros(file_path, 'Departament IT')
    average_salary_in_euros = calculate_average_salary(salary_in_euros)
    write_average_salary_to_cell(file_path, 'Departament IT', average_salary_in_euros)


if __name__ == '__main__':
    exercise_1(r'D:\2xProjects\Python\Project01\IT_dep - Copy.xlsx')
