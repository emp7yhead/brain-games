import random
from braingames.game_engine.game_engine import start_game_round

LOWER_LIMIT = 0
UPPER_LIMIT = 100
RULE_MSG = '"yes" if given number is prime. Otherwise answer "no"'


def generate_prime_mode():
    question = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    correct_answer = 'yes' if is_prime(question) is True else 'no'
    return correct_answer, question


def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def prime_game():
    start_game_round(RULE_MSG, generate_prime_mode)
