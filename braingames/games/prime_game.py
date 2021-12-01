import random
from braingames.game_engine.game_engine import generate_game_round

LOWER_LIMIT = 1
UPPER_LIMIT = 100
RULE_MSG = '"yes" if given number is prime. Otherwise answer "no"'


def generate_prime_mode():
    question = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    correct_answer = 'yes' if is_prime(question) is True else 'no'
    return correct_answer, question


def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def prime_game():
    generate_game_round(RULE_MSG, generate_prime_mode)
