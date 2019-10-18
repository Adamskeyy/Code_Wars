def binary_array_to_number(arr):
    x = len(arr)
    y = []
    for i in range(x):
        if arr[i] > 0:
            y.append(2 ** (x-1))
        x -= 1
    return sum(y)


print(binary_array_to_number([1, 0, 0, 1]))