def change(array):
    array.sort()
    total = 0
    for num in array:
        if num > total + 1:
            return total + 1
        total += array[num]
    return total + 1
        