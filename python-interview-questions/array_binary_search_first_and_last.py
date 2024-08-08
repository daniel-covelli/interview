from helpers.test import validate
from math import ceil

inputs = [
    [
        8,
        [5, 7, 7, 8, 8, 10]
    ],
    [
        1,
        [1]
    ],
    [
        1,
        [1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    ],
    [
        8,
        [5, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8]
    ]
]

outputs = [
    [3, 4],
    [0, 0],
    [0, 4],
    [3, 11]
]

def find_first_and_last(target, array):
    first = 0
    last = len(array) - 1
    index = 0
    while last - first > 0:
        middle = ceil((last - first) / 2)
        if array[middle] == target:
            index = middle
            break
        elif target > array[middle]:
            first = middle + 1
        else:
            last = middle - 1
    left = index
    right = index
    while left - 1 >= 0 and target == array[left - 1]:
        left -= 1
    while right + 1 <= len(array) - 1 and target == array[right + 1]:
        right += 1
    return [left, right]

validate(find_first_and_last, inputs, outputs)