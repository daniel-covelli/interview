from collections import deque

# Complex Example 1
# 4 > 5 > 6 > 11 > 12
#     v            ^
#     7            13
#     v            ^
# 1 > 2 > 8 > 9  > 10

# 4 > 5 > 1 > 7 > 2 > 8 > 9 > 10 > 11 > 13 > 12

# Complex example 2
#     4
#     v
# 1 > 2 < 3 < 6
#     ^
#     5

#  1 > 3 > 4 > 5 > 2

# Thoughts:
#   - Need a dict w parent: children pairs
#   and dict w child: parents pairs
#   - start w nodes that do not have a parent
#       - these nodes are considered available
#   - look at this nodes children
#       - if nodes child does not have any other parents add this child to available
#       - if nodes child has other parents that have not been seen it is not yet available

inputs = [
    # Complex Example 1
    [
        [4, 5],
        [5, 6],
        [5, 7],
        [1, 2],
        [7, 2],
        [2, 8],
        [6, 11],
        [8, 9],
        [9, 10],
        [10, 13],
        [13, 12],
        [11, 12]
    ],
    # Complex Example 2
    [
        [4, 2],
        [1, 2],
        [3, 2],
        [5, 2],
        [6, 3]
    ],
    [
        [1, 2],
        [2, 3]
    ],
    [
        [1, 2]
    ]
]

def create_dictionaries(graph):
    parent_children = {}
    child_parents = {}
    for [p, c] in graph:
        if p in parent_children:
            parent_children[p].add(c)
        else:
            parent_children[p] = set([c])
        if c in child_parents:
            child_parents[c].add(p)
        else:
            child_parents[c] = set([p])
    starting_points = []
    for pair in graph:
        if pair[0] not in child_parents:
            starting_points.append(pair[0])
    return [parent_children, child_parents, starting_points]

def valid_dependency_chain(graph):
    [parent_children, child_parents, starting_points] = create_dictionaries(graph)
    seen = set()
    available = deque(starting_points)
    results = []
    while available:
        curr_parent = available.popleft()
        seen.add(curr_parent)
        results.append(curr_parent)
        if curr_parent not in parent_children:
            continue
        for c in parent_children[curr_parent]:
            parents_seen = True
            for p in child_parents[c]:
                if p not in seen:
                    parents_seen = False
                    break
            if not parents_seen:
                break
            else:
                available.append(c)
    return results

for input in inputs:
    print(valid_dependency_chain(input))
