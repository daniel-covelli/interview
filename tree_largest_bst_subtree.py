from helpers.binary_tree import Tree
from helpers.test import validate

inputs = [Tree([10, 5, 15, 1, 8, None, 7]).root, Tree([10, 8, 12, 7, None, 11, 13]).root, Tree([1, None, 2, None, 3, None, -1]).root, Tree([1, -1, None, None, 3]).root, Tree([10, 5, 11, 3, None, 2, None]).root]

def largest_bst_subtree(root):
    count = 0
    def dfs(node, max, min):
        nonlocal count
        return count

    dfs(root, root.val, root.val)
    return count

outputs = [3, 6, 3, 2, 3]

validate(largest_bst_subtree, inputs, outputs)