from demo import *
import random


def test_max_min():
    for n in range(10000):
        arr = []
        for n in range(10):
            arr.append(random.randint(10, 100))

        m = max_min(arr)

        for x in arr:
            assert(m >= x)
