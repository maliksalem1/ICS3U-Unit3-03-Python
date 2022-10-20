#!/usr/bin/env python3

# Created by: maliksalem1
# Created on: Oct 2022
# This program sees if you guess the right number

import random


def main():
    # This function sees if you guessed right or wrong

    # Input
    guessed_number = int(input("Enter the number between 0-9: "))
    print("")

    # Process and Output
    random_variable = random.randint(0, 9)
    if guessed_number == random_variable:
        print("You guessed right.")
    else:
        print("You guessed wrong, the number was {0}.".format(random_variable))

    print("\nDone.")


if __name__ == "__main__":
    main()
