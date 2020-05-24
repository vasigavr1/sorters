import math

from src.generic_util import swap_positions


def merge(lhs_array: list, rhs_array, lhs_size: int, rhs_size: int):
    # print("lhs: {0}, rhs: {1}".format( str(lhs_size), str(rhs_size)))
    # print(lhs_array)
    # print(rhs_array)
    s_arr_size = lhs_size + rhs_size
    lhs_ptr = 0
    rhs_ptr = 0
    sorted_array = []
    for i in range(s_arr_size):
        # if the element of the left-hand-side array is smaller, insert it
        if lhs_ptr < lhs_size and \
                (rhs_ptr == rhs_size or lhs_array[lhs_ptr] <= rhs_array[rhs_ptr]):
            # print("LHS insert "+ str(lhs_ptr)+ " in " + str(i))
            # print(str(lhs_array[lhs_ptr]))
            sorted_array.append(lhs_array[lhs_ptr])
            lhs_ptr += 1
        else:
            # print("RHS insert " + str(rhs_ptr) + " in " + str(i))
            sorted_array.append(rhs_array[rhs_ptr])
            rhs_ptr += 1
    print(sorted_array)
    return sorted_array


def merge_sort_recursive(array, size):
    if size == 1:
        return array
    if size == 2:
        if array[0] > array[1]:
            swap_positions(array, 0, 1)
            print(array)
        return array

    rhs_ptr = math.floor(size / 2)
    lhs_array = array[:rhs_ptr]
    rhs_array = array[rhs_ptr:size]
    print("Splitting array")
    print(lhs_array)
    print(rhs_array)
    print("--------------")

    lhs_array = merge_sort_recursive(lhs_array, len(lhs_array))
    rhs_array = merge_sort_recursive(rhs_array, len(rhs_array))
    print("TIME TO merge")
    print(lhs_array)
    print(rhs_array)
    print("--------------")
    print("Lhs size " + str(len(lhs_array)))
    print("Rhs size " + str(len(rhs_array)))
    merged_array = merge(lhs_array, rhs_array, len(lhs_array), len(rhs_array))
    print("AFTER MERGING")
    print(merged_array)
    print("--------------")
    # merged_array = merge(array, lhs, rhs, lhs_size, rhs_size)
    return merged_array


def merge_sort(array):
    size = len(array)
    print(array)
    array[:] = merge_sort_recursive(array, size)
    print(array)
