from helpers.class_tree import Tree
from helpers.test import validate
from collections import deque

inputs = [Tree([10, 5, 15, 1, 8, None, 7]).root, Tree([10, 8, 12, 7, None, 11, 13]).root, Tree([1, None, 2, None, 3, None, -1]).root, Tree([1, -1, None, None, 3]).root, Tree([10, 5, 11, 3, None, 2, None]).root, Tree([]).root]

def largest_bst_subtree(root):
    if root == None:
        return 0
    count = 0
    queue = deque([(root, float('inf'), float('-inf'))])
    while queue:
        levelValid = True
        levelCount = len(queue)
        for _ in range(levelCount):
            [node, maxVal, minVal] = queue.popleft()
            left = node.left
            right = node.right
            if node.val > maxVal or node.val < minVal:
                levelValid = False
                break
            if left != None:
                queue.append((left, node.val, minVal))
            if right != None:
                queue.append((right, maxVal, node.val))
        if levelValid == False:
            break
        count += levelCount
    return count

outputs = [3, 6, 3, 2, 3, 0]

validate(largest_bst_subtree, inputs, outputs)