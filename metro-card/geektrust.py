from sys import argv
from src.metro_card_service import MetroCardService


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        exit(1)


def parse_commands(file_lines):
    commands = []
    for line in file_lines:
        command = line.strip()
        command_words_list = command.split(" ")
        commands.append(command_words_list)
    return commands


def execute_commands(commands, metro_card_service):
    for command in commands:
        first_word = command[0]
        if first_word == "BALANCE":
            metro_card_service.add_card_balance(command[1], int(command[2]))
        elif first_word == "CHECK_IN":
            metro_card_service.perform_check_in(command[1], command[2], command[3])
        elif first_word == "PRINT_SUMMARY":
            metro_card_service.print_summary()
        else:
            print("Invalid input command arguments found.")


def main():
    if len(argv) != 2:
        print("Usage: python script.py <input_file>")
        exit(1)
    file_path = argv[1]
    file_lines = read_file(file_path)
    commands = parse_commands(file_lines)
    metro_card_service = MetroCardService()
    execute_commands(commands, metro_card_service)


if __name__ == "__main__":
    main()
