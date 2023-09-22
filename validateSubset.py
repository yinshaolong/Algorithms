def validateSubset(array, sequence):
    arr_index = 0
    seq_index = 0
    while arr_index < len(array) and seq_index < len(sequence):
        if sequence[seq_index] == array[arr_index]:
            seq_index += 1
        arr_index += 1
    return seq_index == len(sequence)