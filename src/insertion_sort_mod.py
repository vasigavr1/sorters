from typing import Any, Union

import generic_util as gu
import math


def simple_insertion_sort(array):
    size: int = len(array)
    for i in range(size):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                gu.swap_positions(array, j, j - 1)


def binary_search(array, size, begin, end, comp_val):
    assert size > 0
    pos: int = begin + int(size / 2)
    # print("Pos: {0}, Size: {1}, begin: {2}, end {3}, comp_val {4}"
    #       .format(str(pos), str(size), str(begin), str(end), str(comp_val)))
    if size == 1:
        if array[end] >= comp_val and array[begin] <= comp_val:
            return True, end
        elif array[begin] >= comp_val:
            return True, begin
        else:
            return False, end
    # Recursion
    if array[pos] == comp_val:
        return True, pos
    if array[pos] > comp_val:
        # we found at least one -->pos
        return binary_search(array, math.ceil(size / 2), begin, pos, comp_val)
    elif array[pos] < comp_val:
        return binary_search(array, math.ceil(size / 2), pos, end, comp_val)



def binary_insertion_sort(array):
    size: int = len(array)
    for i in range(1, size):
        tup :tuple = (False, i)
        # print(array)
        # print("Inspecting  array[{0}] = {1}".format(str(i), str(array[i])))
        tup = binary_search(array, i, 0, i, array[i])
        pos = tup[1]
        found = tup[0]
        if found:
            # print(
            # "Exchange array[{0}] = {1} with array[{2}] = {3}".format(str(i), str(array[i]), str(pos), str(array[pos])))
            for j in range(i, pos, -1):
                gu.swap_positions(array, j, j - 1)




def insertion_sort(array, binary: bool):
    print(array)
    if binary:
        binary_insertion_sort(array)
    else:
        simple_insertion_sort(array)
    print(array)
