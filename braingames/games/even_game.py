import random
from braingames.functions.func import game_round

LOWER_LIMIT = 1
UPPER_LIMIT = 100
RULE_MSG = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_even_mode():
    question = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    if question % 2 == 0:
        correct_answer = 'yes'
        return correct_answer, question
    else:
        correct_answer = 'no'
        return correct_answer, question


def even_game():
    game_round(RULE_MSG, generate_even_mode)
