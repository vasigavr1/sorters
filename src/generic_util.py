def swap_positions(array: list, pos1: int, pos2: int):
    array[pos1], array[pos2] = array[pos2], array[pos1]
    return array