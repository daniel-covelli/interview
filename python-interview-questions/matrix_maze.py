from helpers.test import validate

inputs = [
    [
        [
            [0,0,1,0,0],
            [0,0,0,0,0],
            [0,0,0,1,0],
            [1,1,0,1,1],
            [0,0,0,0,0]
        ],
        [0, 4],
        [4, 4]
    ],
    [
        [
            [0,0,1,0,0],
            [0,0,0,0,0],
            [0,0,0,1,0],
            [1,1,0,1,1],
            [0,0,0,0,0]
        ],
        [0, 4],
        [3, 2]
    ],
    [
        [
            [0,0,0,0,0],
            [1,1,0,0,1],
            [0,0,0,0,0],
            [0,1,0,0,1],
            [0,1,0,0,0]
        ],
        [4, 3],
        [0, 1]
    ],
    [
        [
            [0,0,1,0,0],
            [0,0,0,0,0],
            [0,0,0,1,0],
            [1,1,0,1,1],
            [0,0,0,0,0]
        ],
        [0,4],
        [1, 2]
    ]
]

outputs = [True, False, False, True]


def hasPath(maze, start, destination):
    directions = [[0, 1], [0 , -1], [1, 0], [-1, 0]]
    m = len(maze)
    n = len(maze[0])
    seen = [[0 for _ in range(n)] for _ in range(m)]
    seen[start[0]][start[1]] = 1
    stack = [start]

    def inbounds(r, c):
        return r < m and r >= 0 and c < n and c >= 0

    def hasEligibleNeighbor(r, c):
        return inbounds(r, c) and seen[r][c] != 1 and maze[r][c] != 1

    while len(stack):
        currentLength = len(stack)
        for _ in range(currentLength):
            [nextr, nextc] = stack.pop()
            for [dirr, dirc] in directions:
                r = nextr + dirr
                c = nextc + dirc
                if hasEligibleNeighbor(r, c):
                    seen[r][c] = 1
                    if [r,c] == destination:
                        for [dirr, dirc] in directions:
                            nr = r + dirr
                            nc = c + dirc
                            if hasEligibleNeighbor(nr, nc):
                                return False
                        return True
                    stack.append([r, c])
    return False

validate(hasPath, inputs, outputs)




