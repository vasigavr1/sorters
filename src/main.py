from math import *  # floor(), ceil(), sqrt()
import heap_sort_mod, merge_sort_mod, insertion_sort_mod, BST_sort_mod
from random import randint, seed


def main():
    print("python main function")
    seed(1)
    array = []
    size: int = 100
    max_value: int = size
    for pos in range(size):
        new_number = randint(0, max_value + 1)
        #print("array[" + str(pos) + "] = " + str(new_number))
        array.append(new_number)

    array_heap_sorted = array.copy()
    array_insertion_sorted = array.copy()
    array_merge_sorted = array.copy()
    array_BST_sorted = array.copy()

    # heap_sort_mod.heap_sort(array_heap_sorted)
    # insertion_sort_mod.insertion_sort(array_insertion_sorted, True)
    #merge_sort_mod.merge_sort(array_merge_sorted)
    BST_sort_mod.BST_sort(array_BST_sorted)

    # TEST
    array.sort()
    #print(array)
    #assert array_merge_sorted == array
    #assert array == array_heap_sorted == array_insertion_sorted
    assert array_BST_sorted == array

if __name__ == '__main__':
    main()
