from math import *  # floor(), ceil(), sqrt()
import heap_sort_mod
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

    heap_sort_mod.heap_sort(array, size)


if __name__ == '__main__':
    main()
