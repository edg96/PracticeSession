import csv


def prompt_user_credentials() -> tuple[str, str]:
    """
    Prompt the user for their credentials.

    Returns:
        tuple[str, str]: A tuple containing the username and password credentials that the user entered as input.
    """
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    return username, password


def check_user_credentials(file_path: str, username: str, password: str) -> bool:
    """
    Check the user credentials from the CSV file meant to be a login phase.

    Parameters:
        file_path (str): The path to the CSV file.
        username (str): The username credential of the user.
        password (str): The password credential of the user.

    Returns:
        bool: A boolean value indicating if the user passed the login phase or not.
    """
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['User'] == username and row['Password'] == password:
                return True
        return False


def read_names_from_csv(file_path: str):
    """
    Read and print the content of a CSV file.

    Parameters:
        file_path (str): The path to the CSV file.
    """
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row)


def get_user_input() -> dict[str, str]:
    """
    Get user input for user, password, first name, last name and email.

    Returns:
        dict[str, str]: A dictionary containing user input for first name, last name,
            user, password, and email.
    """
    user = input('Enter your user: ')
    password = input('Enter your password: ')
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    email = input('Enter your email: ')

    user_data = {
        'First_name': first_name,
        'Last_name': last_name,
        'User': user,
        'Password': password,
        'Email': email
    }

    return user_data


def register_new_entry_csv(file_path: str, user_data: dict):
    """
    Append user data to the CSV file.

    Parameters:
        file_path (str): The path to the CSV file.
        user_data (dict): A dictionary containing user data.
    """
    with open(file_path, 'a', newline='') as csvfile:
        headers = ['User', 'Password', 'First_name', 'Last_name', 'Email']
        writer = csv.DictWriter(csvfile, fieldnames=headers)

        # If the file is empty, write the header first
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write the new row
        writer.writerow(user_data)


def welcome_user(username: str):
    """
    Print a welcome message to the user.

    Parameters:
        username (str): The username of the user.
    """
    print(f'Welcome {username}!')


def print_user_information(file_path: str, username: str):
    """
    Read and print the content of a CSV file for a specific user.

    Parameters:
        file_path (str): The path to the CSV file.
        username (str): The username of the user.
    """
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['User'] == username:
                print(row)
                break


def main_menu():
    """
    Display the main menu options.
    """
    print('No such user in use. Would you like to register?')
    print('1. Yes, I would like to.')
    print('2. No, I want to exit.')
    choice = input('Enter your choice: ')
    return choice


def exercise_3(file_path: str):
    """
    Perform the login phase or register a new user if they want to.

    Parameters:
        file_path (str): The path to the CSV file.
    """
    username, password = prompt_user_credentials()
    login_phase_status = check_user_credentials(file_path, username, password)
    if login_phase_status:
        welcome_user(username)
        print_user_information(file_path, username)
    else:
        choice = main_menu()
        if choice == '1':
            user_data = get_user_input()
            register_new_entry_csv(file_path, user_data)
            print('Registration completed.')
        print('Goodbye!')


if __name__ == '__main__':
    pass
