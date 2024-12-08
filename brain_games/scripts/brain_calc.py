#!/usr/bin/env python3
import random
from re import A
from urllib.parse import _NetlocResultMixinBase
import prompt

# from .cli import welcome_user

def main():
    # number = random.randint(1, 40)
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    print('What is the result of the expression?')
    i = 1
    while i <= 3:
        number_one = random.randint(10, 40)
        number_two = random.randint(1, 10)
        operator = ['*', '+', '-']
        random_index = random.randint(0, len(operator) - 1)
        random_element = operator[random_index]
        print(f"Question {number_one} {random_element} {number_two}")
        n = input(("Your answer: "))
        if random_element == "*" and str(number_one * number_two) == n:
            print("Correct!")
        elif random_element == "+" and str(number_one + number_two) == n:
            print("Correct!")
        elif random_element == "-" and str(number_one - number_two) == n:
            print("Correct!")
        else:
            if random_element == '*':
                answer = number_one * number_two
            elif random_element == "+":
                answer = number_one + number_two
            elif random_element == "-":
                answer = number_one - number_two
            print(f"'{n}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}!")
            break
        if i == 3:
            print(f"Congratulations, {name}!")
        i += 1

    


if __name__ == "__main__":
    main()