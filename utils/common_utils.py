import string
import random
import datetime


def rnd_string_gen(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def get_current_datetime():
    return ''.join(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

