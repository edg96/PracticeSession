from practicesession15essentials import get_workbook


def get_salary_values(file_path: str, sheet_name: str) -> list[int]:
    """
    Extracts salary values in euros from the specified worksheet.

    Parameters:
        file_path (str): The file path to the Excel file.
        sheet_name (str): The name of the worksheet containing salary information.

    Returns:
        list[int]: A list of salary values in euros.
    """
    workbook = get_workbook(file_path)
    sheet = workbook[sheet_name]
    salary_values = [row[3] for row in sheet.iter_rows(min_row=2, values_only=True)]

    return salary_values


def calculate_average_salary(salary_values: list) -> int:
    """
    Calculates the average salary in euros from the provided list of salary values.

    Parameters:
        salary_values (list): A list of salary values in euros.

    Returns:
        int: The calculated average salary in euros.
    """
    total_value_in_euros = sum(salary_values)
    average_salary_in_euros = total_value_in_euros // len(salary_values)

    return average_salary_in_euros


def write_average_salary_to_cell(file_path: str, sheet_name: str, average_salary_in_euros: int):
    """
    Writes the average salary value in euros to cell D14 in the specified worksheet.

    Parameters:
        file_path (str): The file path to the Excel file.
        sheet_name (str): The name of the worksheet to write to.
        average_salary_in_euros (int): The average salary value in euros to write.
    """
    workbook = get_workbook(file_path)
    sheet = workbook[sheet_name]
    sheet['D14'] = average_salary_in_euros

    workbook.save(file_path)
