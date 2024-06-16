from helpers.class_tree import Tree
from helpers.test import validate
from collections import deque

inputs = [Tree([]).root, Tree([3, 9, 20, None, None, 15, 7]).root, Tree([1]).root, Tree([1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, 10, 11]).root]

def zigzag(root):
    if not root:
        return []

    results = []
    queue = deque([(root, 0)])

    while queue:
        length = len(queue)
        result = deque([])
        shouldReverse = queue[0][1] % 2 != 0
        for _ in range(length):
            [node, level] = queue.popleft()
            if shouldReverse:
                result.appendleft(node.val)
            else:
                result.append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        results.append(list(result))
    return results

outputs = [[], [[3], [20, 9], [15, 7]], [[1]], [[1], [3, 2], [4, 5, 6, 7], [11, 10, 9, 8]]]

validate(zigzag, inputs, outputs)