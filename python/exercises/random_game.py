from sys import argv
from random import randint


def main():
    num1, num2 = input_checking()
    random_number = randint(num1, num2)
    print(random_number)


def input_checking():
    if len(argv) != 3:
        print_usage()
    try:
        num1 = int(argv[1])
        num2 = int(argv[2])
    except ValueError:
        print("Inputs must be numbers.")
        print_usage()
    if num1 < 1 or num2 < 1:
        print("Input numbers must be greater than 0.")
        print_usage()
    if num1 > num2:
        print("Start_number must be less than end_number.")
        print_usage()

    return (num1, num2)


def print_usage():
    print("Usage: random_game.py start_number end_number")
    quit()


if __name__ == "__main__":
    main()
