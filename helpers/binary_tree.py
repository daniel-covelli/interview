from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, vals):
        self.root = self.__generateTree(vals)

    def __generateTree(self, vals):
        if len(vals) == 0:
            return None
        root = Node(vals[0])
        queue = deque([root])
        vals = deque(vals[1:])
        while queue:
            curr = queue.popleft()
            left = vals.popleft() if len(vals) else None
            right = vals.popleft() if len(vals) else None
            if left != None:
                node = Node(left)
                curr.left = node
                queue.append(node)
            if right != None:
                node = Node(right)
                curr.right = node
                queue.append(node)
        return root

    def printTree(self):
        if self.root is None:
            return []
        results = []
        queue = deque([self.root])
        results.append(self.root.val)
        while queue:
            curr = queue.popleft()
            if curr.left == None and curr.right == None:
                continue
            if curr.left != None:
                results.append(curr.left.val)
                queue.append(curr.left)
            if curr.left == None:
                results.append(None)
            if curr.right != None:
                results.append(curr.right.val)
                queue.append(curr.right)
            if curr.right == None:
                results.append(None)

        return results
