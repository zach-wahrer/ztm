from sys import argv
from random import randint


def main():
    num1, num2 = cl_input_checking()
    random_number = randint(num1, num2)

    try:
        while True:
            guess = guess_checking(input("What is your guess?: "), num1, num2)
            if guess == random_number:
                print(f"You win! You guessed the random number: {random_number}.")
                break
            elif guess is None:
                print("Try again.")
            else:
                print(f"{guess} is not the random number. Try again.")
    except EOFError:
        print("\nGiving up so soon?")
        quit()


def guess_checking(guess, num1, num2):
    try:
        guess = int(guess)
    except ValueError:
        print("Guess must be a number.")
        return None
    if guess < num1 or guess > num2:
        print(f"Your guess must be within the range of {num1} and {num2}.")
        return None
    return guess


def cl_input_checking():
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
    if num1 >= num2:
        print("Start_number must be less than end_number.")
        print_usage()

    return (num1, num2)


def print_usage():
    print("Usage: random_game.py start_number end_number")
    quit()


if __name__ == "__main__":
    main()
