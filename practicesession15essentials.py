import openpyxl


def get_workbook(file_path: str) -> openpyxl.Workbook:
    """
    Load and returns the Excel file from the specified path using OpenPyXl workbook.

    Parameters:
        file_path (str): The file path to the Excel file.

    Returns:
        openpyxl.Workbook: The OpenPyXl workbook object representing the loaded Excel file.
    """
    workbook = openpyxl.reader.excel.load_workbook(file_path)

    return workbook
