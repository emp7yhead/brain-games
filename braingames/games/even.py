import random
from braingames.game_engine.game_engine import start_game_round

LOWER_LIMIT = 1
UPPER_LIMIT = 100
RULE_MSG = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_even_mode():
    question = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question


def even_game():
    start_game_round(RULE_MSG, generate_even_mode)
