import random
from braingames.functions.func import game_round

LOWER_LIMIT = 1
UPPER_LIMIT = 100
RULE_MSG = '"yes" if given number is prime. Otherwise answer "no"'


def game_mode():
    question = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    correct_answer = is_prime(question)
    return correct_answer, question


def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return 'no'
    return 'yes'


def prime_game():
    game_round(RULE_MSG, game_mode)
