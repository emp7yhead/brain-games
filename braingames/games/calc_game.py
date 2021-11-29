import random
from braingames.functions.func import game_round

LOWER_LIMIT = 1
UPPER_LIMIT = 100
RULE_MSG = 'What is the result of the expression?'
OPERATORS = '+', '-', '*'


def generate_calc_mode():
    random_num1 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    random_num2 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    operator = random.choice(OPERATORS)
    question = str(random_num1) + ' ' + operator + ' ' + str(random_num2)
    if operator == '+':
        correct_answer = random_num1 + random_num2
    elif operator == '-':
        correct_answer = random_num1 - random_num2
    elif operator == '*':
        correct_answer = random_num1 * random_num2
    return str(correct_answer), question


def calc_game():
    game_round(RULE_MSG, generate_calc_mode)
