import random
import prompt
import math


def brain_gcd():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    print('Find the greatest common divisor of given numbers.')
    i = 1
    while i <= 3:
        number_one = random.randint(2, 100)
        number_two = random.randint(2, 100)
        print(f"Question: {number_one} {number_two}")
        n = input("Your answer: ")
        if str(math.gcd(number_one, number_two)) == n:
            print("Correct!")
        else:
            result = math.gcd(number_one, number_two)
            print(f"'{n}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
            break
        if i == 3:
            print(f"Congratulations, {name}!")
        i += 1


if __name__ == "__brain_gcd__":
    brain_gcd()