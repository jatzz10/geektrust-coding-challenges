from sys import argv
from src.metro_card_service import MetroCardService
from src.constants import (ARGUMENTS_LENGTH, EXIT_FILE_NOT_FOUND, BALANCE_ARGS_LENGTH, CHECK_IN_ARGS_LENGTH,
                           INPUT_COMMAND_CARD_ID_INDEX, INPUT_COMMAND_BALANCE_INDEX, INPUT_COMMAND_PASSENGER_TYPE_INDEX,
                           INPUT_COMMAND_STATION_NAME_INDEX, FILE_PATH_ARGUMENT_INDEX, INPUT_COMMAND_FIRST_WORD_INDEX)


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        exit(EXIT_FILE_NOT_FOUND)


def parse_commands(file_lines):
    commands = []
    for line in file_lines:
        command = line.strip()
        command_words_list = command.split(" ")
        commands.append(command_words_list)
    return commands


def execute_commands(commands, metro_card_service):
    for command in commands:
        first_word = command[INPUT_COMMAND_FIRST_WORD_INDEX]
        if first_word == "BALANCE" and len(command) == BALANCE_ARGS_LENGTH:
            metro_card_service.add_card_balance(command[INPUT_COMMAND_CARD_ID_INDEX], int(command[INPUT_COMMAND_BALANCE_INDEX]))
        elif first_word == "CHECK_IN" and len(command) == CHECK_IN_ARGS_LENGTH:
            metro_card_service.perform_check_in(command[INPUT_COMMAND_CARD_ID_INDEX], command[INPUT_COMMAND_PASSENGER_TYPE_INDEX], command[INPUT_COMMAND_STATION_NAME_INDEX])
        elif first_word == "PRINT_SUMMARY":
            metro_card_service.print_summary()
        else:
            print("Invalid input command arguments found.")


def main():
    if len(argv) != ARGUMENTS_LENGTH:
        print("Usage: python script.py <input_file>")
        exit(EXIT_FILE_NOT_FOUND)
    file_path = argv[FILE_PATH_ARGUMENT_INDEX]
    file_lines = read_file(file_path)
    commands = parse_commands(file_lines)
    metro_card_service = MetroCardService()
    execute_commands(commands, metro_card_service)


if __name__ == "__main__":
    main()
