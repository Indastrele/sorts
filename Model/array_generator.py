import random


def generate(left_border, right_border, size):
    arr = list()
    for i in range(0, size):
        arr.append(random.randint(left_border, right_border + 1))

    return arr
