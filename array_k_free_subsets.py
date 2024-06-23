from helpers.test import validate

'''
You are given an integer array nums, which contains distinct elements and an integer k.

A subset is called a k-Free subset if it contains no two elements with an absolute difference equal to k. Notice that the empty set is a k-Free subset.

Return the number of k-Free subsets of nums.

A subset of an array is a selection of elements (possibly none) of the array.
'''

inputs = [
    [
        [5,4,6], 1
    ],
    [
        [2, 3, 5, 8], 5
    ]
]

outputs = [5, 12]

def k_free_subs(nums, k):
    return 0

validate(k_free_subs, inputs, outputs)