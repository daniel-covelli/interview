from helpers.binary_tree import Tree
from helpers.test import validate
from collections import deque
'''
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
'''
inputs = [[Tree([10,5,-3,3,2,None,11,3,-2,None,1]).root, 8], [Tree([5,4,8,11,None,13,4,7,2,None,None,5,1]).root, 22]]

def pathSum(root, targetSum):
    count = 0
    def dfs(node, sums):
        nonlocal count
        if node == None:
            return
        if sums[-1] == targetSum:
            count += 1
        sums.append(sums[-1] + node.val)
        dfs(node.left, sums)
        dfs(node.right, sums)



    dfs(root, [root.val])
    return count




outputs = [3, 3]

validate(pathSum, inputs, outputs)