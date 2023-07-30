def read_accounts_from_txt(file_path: str) -> list[str]:
    """
    Read accounts from a text file.

    Parameters:
        file_path (str): The path to the text file containing accounts.

    Returns:
        list[str]: A list of accounts read from the text file.
    """
    with open(file_path, 'r') as txt_file:
        accounts = txt_file.read().split()

    return accounts


def check_user_credentials(accounts: list[str], username: str, password: str) -> bool:
    """
    Check if user credentials are valid.

    Parameters:
        accounts (list[str]): A list of accounts in the format 'user:username passwd:password'.
        username (str): The username to check.
        password (str): The password to check.

    Returns:
        bool: True if the user credentials are valid, False otherwise.
    """
    username = 'user:' + username
    password = 'passwd:' + password
    for account in accounts:
        if username in account and password in account:
            return True
    return False


def exercise_2(file_path: str, username: str, password: str) -> bool:
    """
    This function reads accounts from a text file, checks if the given username and password
    match any of the accounts, and returns True if the credentials are valid, False otherwise.

    Parameters:
        file_path (str): The path to the text file containing accounts.
        username (str): The username to check.
        password (str): The password to check.

    Returns:
        bool: True if the user credentials are valid, False otherwise.
    """
    accounts = read_accounts_from_txt(file_path)
    successful_login = check_user_credentials(accounts, username, password)

    return successful_login


if __name__ == '__main__':
    pass
