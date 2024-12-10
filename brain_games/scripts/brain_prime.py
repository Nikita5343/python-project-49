#!/usr/bin/env python3
import random
import prompt

def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    for i in range(2,int(number)):
        if number % i == 0:
            return False
        else:
            return True

def brain_prime():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 1
    while i <= 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        n = input("Your answer: ")
        if is_prime(number) and n == 'yes':
            print("Correct!")
        elif is_prime(number) == False and n == "no":
            print("Correct!")
        else:
            if is_prime(number):
                result = 'yes'
            else:
                result = 'no'
            print(f"'{n}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")
            break
        if i == 3:
            print(f"Congratulations, {name}!")
        i += 1


if __name__ == "__brain_prime__":
    brain_prime()

# if __name__ == "brain_even":
#     brain_even()

