

import random


def get_random(num):
    return random.randint(num, num**2)


for value in range(10,24):
    answer = get_random(value)
    print(answer)

