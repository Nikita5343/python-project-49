#!/usr/bin/env python3
import random
import prompt

from .cli import welcome_user


def main():
    number = random.randint(1, 100)
    # is_even = number % 2 == 0
    # is_not_even = number % 2 != 0
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    while i <= 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        n = input("Your answer: ")
        if number % 2 == 0 and n == 'yes':
            print("Correct!")
        elif number % 2 != 0 and n == "no":
            print("Correct!")
        else:
            if number % 2 == 0:
                result = 'yes'
            else:
                result = 'no'
            print(f"'{n}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
            break
        if i == 3:
            print(f"Congratulations, {name}!")
        i += 1


if __name__ == "__main__":
    main()

# if __name__ == "brain_even":
#     brain_even()

