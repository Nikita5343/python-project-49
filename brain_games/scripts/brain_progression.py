#!/usr/bin/env python3
import random
import prompt

from .cli import welcome_user


def brain_progression():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    print('What number is missing in the progression?')
    i = 1
    while i <= 3:
        result = ''
        for i in range(random.randint(1, 50), random.randint(50, 100), random.randint(2, 8)):
            if result:
                result += " "
            result += i
        print(result)
        if i == 3:
            print(f"Congratulations, {name}!")
        i += 1


if __name__ == "__brain_progression__":
    brain_progression()

# if __name__ == "brain_even":
#     brain_even()

