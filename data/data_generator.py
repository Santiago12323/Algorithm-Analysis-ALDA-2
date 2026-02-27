import random
from data import constants
def get_random_list(size, limit=constants.MAX_VALUE):
    return list(range(1, size + 1))
def get_random_x(limit=constants.MAX_VALUE):
    return random.randint(1, limit)


