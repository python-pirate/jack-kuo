from demo import *

def test_max_min():
    arr = []
    for n in range(10):
        arr.append(random.randint(10, 100))
    
    m = max_min(arr)

    for x in arr:
        assert(max >= x)
