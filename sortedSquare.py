def sortedSquare(array):
    left = 0
    right = len(array) -1
    sqArray = [0 for _ in array]
    for num in reversed(range(len(array))):
        if abs(array[left]) > abs(array[right]):
            array[num] = array[left] * array[left]
            left += 1
        else:
            array[num] = array[right] * array[right]
            right -= 1
    return sqArray