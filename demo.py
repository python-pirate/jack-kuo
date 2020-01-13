def max_min(arr):
    m = 0
    i = 1

    while i < len(arr):
        if arr[i] > arr[m]:
            m = i
        i += 1

    return arr[m]
