import generic_util as gu


def max_heapify(array: list, pos: int, size: int):
    # print("Max-heapifying at i = {0}, size: {1}, val: {2}".format(str(pos), str(size), str(array[pos])))
    if pos > size / 2: return
    left_i = (pos * 2) + 1
    right_i = ((pos + 1) * 2)
    greater_pos: int = pos
    if left_i < size and array[left_i] > array[greater_pos]:
        greater_pos = left_i
    if right_i < size and array[right_i] > array[greater_pos]:
        greater_pos = right_i

    if greater_pos != pos:
        # print("greater pos: array[{0}] = {1} > array[{2}] = {3} = ".
        #   format(str(greater_pos), str(array[greater_pos]), str(pos), str(array[pos])))
        gu.swap_positions(array, pos, greater_pos)
        max_heapify(array, greater_pos, size)


def build_max_heap(array: list, size: int):
    for pos in range(int(size / 2), -1, -1):
        max_heapify(array, pos, size)


def heap_sort(array: list):
    print(array)
    size = len(array)
    build_max_heap(array, size)
    for i in range(1, size):
        gu.swap_positions(array, 0, size - i )
        max_heapify(array, 0, size - i)
    print(array)
