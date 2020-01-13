def max_min(arr):
    m = arr[0]
    i = 1

    while i < len(arr):
        if arr[i] > m:
            m = arr[i]
        i += 1

    return m
