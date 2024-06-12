from helpers.binary_tree import Tree
from helpers.test import validate

inputs = [Tree([1, 2, 3]).root, Tree([1, 2, 3, 5, 6, 7, 8, 9, 10]).root, Tree([]).root]

def maximum_depth(root):
    if root == None:
        return 0
    max_depth = 0
    def dfs(node, depth):
        nonlocal max_depth
        if node == None:
            return 0
        max_depth = max(max_depth, depth)
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 1)
    return max_depth

outputs = [2, 4, 0]

validate(maximum_depth, inputs, outputs)