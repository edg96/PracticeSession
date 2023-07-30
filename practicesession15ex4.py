from practicesession15essentials import get_workbook


def get_salaries_in_euros(file_path: str, sheet_name: str) -> list:
    """
    Gets the list of salaries in euros using an OpenPyXl workbook object containing the
        according information in a specified sheet.

    Parameters:
        file_path (str): The file path to the Excel file.
        sheet_name (str): The name of the sheet containing the salary information.

    Returns:
        list: A list containing the salaries in euros.
    """
    workbook = get_workbook(file_path)
    it_department_information = workbook[sheet_name]
    salaries_in_euros = [row[3] for row in it_department_information.iter_rows(min_row=2, values_only=True)]

    return salaries_in_euros


def salary_euros_to_ron(salaries_in_euros: list[int]) -> list[int]:
    """
    Converts the salaries from euro to ron.

    Parameters:
        salaries_in_euros (list[int]): The salaries in euro.

    Returns:
        list: The list of salaries converted from euro to ron.
    """
    salaries_in_ron = [salary * 5 for salary in salaries_in_euros]

    return salaries_in_ron


def create_ron_converted_column(file_path: str, sheet_name: str, column_index: int,
                                header: str, values_to_insert: list[int]):
    """
    Creates a new column in the Excel file located at the specified path, in the according
        sheet name and at the specified index containing the header name and the integer
        values that needs to be inserted at the provided location.

    Parameters:
        file_path (str): The file path to the Excel file.
        sheet_name (str): The sheet where the information needs to be saved.
        column_index (int): The index of the column where the information needs to be saved.
        header (str): The name of the header of the column where the information needs to be saved.
        values_to_insert (list[int]): The list of the values that needs to be saved.
    """
    workbook = get_workbook(file_path)
    sheet = workbook[sheet_name]
    sheet.insert_cols(column_index)
    sheet.cell(row=1, column=column_index, value=header)

    for row_index, value in enumerate(values_to_insert, start=2):
        sheet.cell(row=row_index, column=column_index, value=value)

    workbook.save(file_path)
