from demo import *
import random

def test_select_sort():
    a = [random.randint(10, 100) for _ in range(10)]

    select_sort(a)

    i = 0
    while i < len(a) - 1:
        assert(a[i] <= a[i + 1])
        i += 1
