def select_sort(arr):
    j = len(arr)
    while j > 1:
        m = 0
        i = 1

        while i < j:
            if arr[i] > arr[m]:
                m = i
            i += 1
        if m != i - 1:
            arr[m], arr[i - 1] = arr[i - 1], arr[m]
        j -= 1
