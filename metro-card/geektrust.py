from sys import argv
from src.passenger import Passenger
from src.metro_card import MetroCard
from src.metro_card_service import MetroCardService


def main():
    """
    Sample code to read inputs from the file

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    //Add your code here to process the input commands
    """
    mc1 = MetroCard('MC1', 500)
    ps1 = Passenger('ADULT')
    metro_card_service = MetroCardService(mc1, ps1)
    metro_card_service.check_in('CENTRAL')
    print(mc1, ps1, metro_card_service)


if __name__ == "__main__":
    main()
