import random
from braingames.functions.func import game_round

LOWER_LIMIT = 1
UPPER_LIMIT = 100
STEP_LOWER_LIMIT = 2
STEP_UPPER_LIMIT = 9
LENGHT_LOWER_LIMIT = 6
LENGHT_UPPER_LIMIT = 11
START_LOWER_LIMIT = 1
START_UPPER_LIMIT = 5
RULE_MSG = 'What number is missing in the progression?'


def game_mode():
    step = random.randint(STEP_LOWER_LIMIT, STEP_UPPER_LIMIT)
    lenght = random.randint(LENGHT_LOWER_LIMIT, LENGHT_UPPER_LIMIT)
    slice_start = random.randint(START_LOWER_LIMIT, START_UPPER_LIMIT)
    slice_finish = slice_start + lenght

    generated_question = [i for i in range(LOWER_LIMIT, UPPER_LIMIT, step)]
    list_of_question = generated_question[slice_start:slice_finish]
    secret = random.randint(LOWER_LIMIT, len(list_of_question) - 1)
    correct_answer = list_of_question[secret]
    list_of_question[secret] = '..'

    question = ''
    for j in range(len(list_of_question)):
        question += ' ' + str(list_of_question[j])
    return str(correct_answer), question


def progression_game():
    game_round(RULE_MSG, game_mode)
