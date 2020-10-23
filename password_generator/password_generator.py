import random
from .constants import *

options = [UPPERCASE_CHARACTER, LOWERCASE_CHARACTER, SPECIAL_CHARACTER, NUMERICAL_CHARACTER]


def gen_password(length=DEFAULT_PASSWORD_SIZE):
    pwd = ''
    for _ in range(length):
        choice = random.choice(options)
        if choice == UPPERCASE_CHARACTER:
            pwd += gen_up_char()
        elif choice == LOWERCASE_CHARACTER:
            pwd += gen_low_char()
        elif choice == SPECIAL_CHARACTER:
            pwd += gen_sp_char()
        elif choice == NUMERICAL_CHARACTER:
            pwd += gen_int_char()


def gen_up_char():
    chr(random.randint(UPPERCASE_CHARACTER_ASCII_CODE_LOWER_LIMIT, UPPERCASE_CHARACTER_ASCII_CODE_UPPER_LIMIT))


def gen_low_char():
    chr(random.randint(LOWERCASE_CHARACTER_ASCII_CODE_UPPER_LIMIT, LOWERCASE_CHARACTER_ASCII_CODE_UPPER_LIMIT))


def gen_sp_char():
    chr(random.randint(SPECIAL_CHARACTER_ASCII_CODE_LOWER_LIMIT, SPECIAL_CHARACTER_ASCII_CODE_UPPER_LIMIT))


def gen_int_char():
    chr(random.randint(NUMERICAL_CHARACTER_ASCII_CODE_LOWER_LIMIT, NUMERICAL_CHARACTER_ASCII_CODE_UPPER_LIMIT))
