import prompt

WIN_LIMIT = 3
GREETING_MSG = 'Welcome to the Brain Games!'
ASK_NAME_MSG = 'May I have your name? '
HELLO_MSG = 'Hello, {}!'
ANSWER_MSG = 'Your answer: '
CORRECT_MSG = 'Correct!'
SORRY_MSG = ("'{}' is wrong answer ;( Correct answer was '{}'\n"
             "Let's try again, {}!")
CONGRAT_MSG = 'Congratulations, {}!'
QUESTION_MSG = 'Question: {}'


def generate_game_round(RULE_MSG, game_mode):
    win_count = 0
    print(GREETING_MSG)
    username = prompt.string(ASK_NAME_MSG)
    print(HELLO_MSG.format(username))
    print(RULE_MSG)
    while win_count < WIN_LIMIT:
        correct_answer, question = game_mode()
        print(QUESTION_MSG.format(question))
        user_answer = prompt.string(ANSWER_MSG)
        if user_answer == correct_answer:
            win_count += 1
            print(CORRECT_MSG)
        else:
            print(SORRY_MSG.format(user_answer, correct_answer, username))
            return
    print(CONGRAT_MSG.format(username))
