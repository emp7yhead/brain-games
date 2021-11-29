import random
from braingames.functions.func import game_round

LOWER_LIMIT = 1
UPPER_LIMIT = 100
RULE_MSG = 'Find the greatest common divisor of given numbers.'


def generate_gcd_mode():
    random_num1 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    random_num2 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    question = str(random_num1) + ' ' + str(random_num2)
    correct_answer = str(gcd(random_num1, random_num2))
    return correct_answer, question


def gcd(a, b):
    '''calculate greatest common divisor
       using Euclidean algorithm
    '''
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return b if a == 0 else a


def gcd_game():
    game_round(RULE_MSG, generate_gcd_mode)
