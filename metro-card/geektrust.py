from sys import argv

from src.metro_card_service import MetroCardService


def main():
    if len(argv) != 2:
        print("Usage: python script.py <input_file>")
        exit(1)
    file_path = argv[1]
    try:
        with open(file_path, 'r') as file:
            metro_card_service = MetroCardService()

            for line in file:
                command = line.strip()
                command_words_list = command.split(" ")
                first_word = command_words_list[0]

                # Execute business logic
                if first_word == "BALANCE":
                    card_id = command_words_list[1]
                    card_balance = int(command_words_list[2])
                    metro_card_service.add_card_balance(card_id, card_balance)
                elif first_word == "CHECK_IN":
                    card_id = command_words_list[1]
                    passenger_type = command_words_list[2]
                    station_name = command_words_list[3]
                    metro_card_service.perform_check_in(card_id, passenger_type, station_name)
                elif first_word == "PRINT_SUMMARY":
                    metro_card_service.print_summary()
                else:
                    print("Invalid input command arguments found.")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()

#  """
#     Sample code to read inputs from the file
#
#     if len(argv) != 2:
#         raise Exception("File path not entered")
#     file_path = argv[1]
#     f = open(file_path, 'r')
#     Lines = f.readlines()
#     //Add your code here to process the input commands
# """