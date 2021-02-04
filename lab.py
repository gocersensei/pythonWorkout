#!/usr/bin/env python3
import random


def guessing_game():
    target = random.randint(0, 100)
    while True:
        try:
            guess = int(input("your guess please: "))
            if guess == target:
                print("Just right")
                return

            if guess < target:
                print("Too low")
            else:
                print("Too high")
        except ValueError:
            print("Invalid input, try again.")

guessing_game()