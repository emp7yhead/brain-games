#!/usr/bin/env python

import random
import prompt


def generate_number():
    lower_limit = 1
    upper_limit = 1000
    random_integer = random.randint(lower_limit, upper_limit)
    return random_integer


def welcome_user():
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    return username


def is_even():
    random_integer = generate_number()
    if random_integer % 2 == 0:
        correct_answer = 'yes'
        return correct_answer, random_integer
    else:
        correct_answer = 'no'
        return correct_answer, random_integer


def game():
    username = welcome_user()
    win_count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while win_count < 3:
        correct_answer, random_integer = is_even()
        print(f'Question: {random_integer}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            win_count += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;( "
                  f"Correct answer was '{correct_answer}'\n"
                  f"Let's try again, {username}")
            return
    print(f'Congarulation, {username}!')


if __name__ == '__main__':
    game()
