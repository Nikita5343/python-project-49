#!/usr/bin/env python3
import random
import prompt


def brain_progression():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    print('What number is missing in the progression?')
    i = 1
    while i <= 3:
        result = []
        for i in range(random.randint(1, 20), random.randint(50, 80), random.randint(2, 8)):
            result.append(i)
        answer = random.randint(0, len(result) - 1)
        result[answer] = ".."
        result_two = ''
        for i in result:
            if result:
                result_two += " "
            result_two += str(i)
        print(f"Question: {result_two}")
        n = input("Your answer: ")
        if str(answer) == str(n):
            print("Correct")
        else:
            print("No Correct")
        if i == 3:
            print(f"Congratulations, {name}!")
        i += 1


if __name__ == "__brain_progression__":
    brain_progression()
