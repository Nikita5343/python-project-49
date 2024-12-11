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
    # Создаем прогрессию
        result = []
        step = random.randint(2, 8)  # Шаг прогрессии
        start = random.randint(1, 20)  # Начальное значение
        length = random.randint(5, 10)  # Длина прогрессии
        for j in range(length):
            result.append(start + j * step)

    # Выбираем случайное число для пропуска
        answer_index = random.randint(0, len(result) - 1)
        correct_answer = result[answer_index]  # Сохраняем само число
        result[answer_index] = ".."

    # Формируем строку прогрессии вручную
        progression_str = ""
        for num in result:
            progression_str += str(num) + " "

    # Выводим вопрос
        print(f"Question: {progression_str.strip()}")

    # Получаем ответ пользователя
        user_answer = prompt.string("Your answer: ")

    # Проверяем ответ
        if str(correct_answer) == user_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            break

        if i == 3:
            print(f"Congratulations, {name}!")
        i += 1



if __name__ == "__brain_progression__":
    brain_progression()
