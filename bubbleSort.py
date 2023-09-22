def bubbleSort(array):
    while not isSorted:
        isSorted = True
        counter = 0
        for i in range(len(array) -1 - counter):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSorted = False
            counter += 1
    return array