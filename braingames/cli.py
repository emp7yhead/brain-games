#!/usr/bin/env python

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(username))


if __name__ == '__main__':
    welcome_user()
