def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    middle = (left + right) // 2
    while left <= right:
        if target > array[middle]:
            left += 1
        elif target < array[middle]:
            right -= 1
        else:
            return target == array[middle]
    return False

target = 5
array = [1, 2, 3 , 4, 5 , 6, 7, 8, 9, 10]
print(binarySearch(array, target))

