import random
import string


def password_generator(length):
    sample_space = string.ascii_letters + string.digits + string.punctuation
    password = ''.join((random.choice(sample_space) for i in range(length)))
    return password


def clear_screen():
    print('\033[H\033[J')
