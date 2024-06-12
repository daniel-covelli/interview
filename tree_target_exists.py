from helpers.binary_tree import Tree
from helpers.test import validate

inputs = [[Tree([1, 2, 3]).root, 2], [Tree([1, 2, 3]).root, 4], [Tree([1, 2, 3, None, None, 5, 6, 4, None]).root, 4]]

def check_tree(root, target):
    if root == None:
        return False
    if root.val == target:
        return True
    return check_tree(root.left, target) or check_tree(root.right, target)

outputs = [
    True,
    False,
    True
]

validate(check_tree, inputs, outputs)