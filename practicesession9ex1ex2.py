from practicesession9essentials import get_workbook


def get_employees_manager_pair(file_path: str) -> dict[str, str]:
    """
    Gets the employees names and their corresponding manager name.

    Parameters:
        file_path (str): The file path to the Excel file.

    Returns:
        dict[str, str]: A dictionary with the employees names as the keys and their corresponding
            manager names as the values.
    """
    employees_manager_id_pair = get_employees_manager_id_pair(file_path, 'Departament IT')
    managers_names_id_pair = get_managers_names_id_pair(file_path, 'Manager')
    employees_managers = {employee: managers_names_id_pair[employee_id]
                          for employee, employee_id in employees_manager_id_pair.items()}

    return employees_managers


def get_managers_number_of_employees(file_path: str) -> dict[str, int]:
    """
    Gets the managers names and their corresponding number of employees.

    Parameters:
        file_path (str): The file path to the Excel file.

    Returns:
        dict[str, int]: A dictionary with the managers names as keys and their
            corresponding number of employees as the values.
    """
    employees_manager_id_pair = get_employees_manager_id_pair(file_path, 'Departament IT')
    managers_names_id_pair = get_managers_names_id_pair(file_path, 'Manager')
    employees_per_manager = {manager: list(employees_manager_id_pair.values()).count(manager_id)
                             for manager_id, manager in managers_names_id_pair.items()}

    return employees_per_manager


def get_employees_manager_id_pair(file_path: str, sheet_name: str) -> dict[str, int]:
    """
    Gets the employees names and their corresponding manager id using an OpenPyXl workbook
        object containing the according information in a specified sheet.

    Parameters:
        file_path (str): The file path to the Excel file.
        sheet_name (str): The name of the sheet containing the employee information.

    Returns:
        dict[str, int]: A dictionary with the employees names as keys and their corresponding
            manager id as the values.
    """
    workbook = get_workbook(file_path)
    it_department_employees = workbook[sheet_name]
    employees_managers_id = {row[1] + ' ' + row[2]: int(row[5])
                             for row in it_department_employees.iter_rows(min_row=2, values_only=True)}

    return employees_managers_id


def get_managers_names_id_pair(file_path: str, sheet_name: str) -> dict[int, str]:
    """
    Gets the managers ids and their corresponding names using an OpenPyXl workbook object
        containing the according information in a specified sheet.

    Parameters:
        file_path (str): The file path to the Excel file.
        sheet_name (str): The name of the sheet containing the manager information.

    Returns:
        dict[int, str]: A dictionary with the managers ids as keys and their corresponding
            names as the values.
    """
    workbook = get_workbook(file_path)
    managers = workbook[sheet_name]
    managers_id = {int(row[0]): row[1] for row in managers.iter_rows(min_row=2, values_only=True)}

    return managers_id
