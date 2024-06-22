from helpers.test import validate

inputs = [
    [
        [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
    ],
    [
        [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
    ],
    [
        [
            ["0","0"],
            ["0","0"]
        ]
    ]
]

outputs = [1, 3, 0]

def islands(matrix):
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    m = len(matrix)
    n = len(matrix[0])

    seen = [[False for y in range(n)] for x in range(m)]

    def inbounds(r, c):
        return r >= 0 and r < m and c >= 0 and c < n

    def dfs(r, c):
        seen[r][c] = True
        for [dr, dy] in directions:
            new_r = r + dr
            new_y = c + dy
            if inbounds(new_r, new_y) and not seen[new_r][new_y] and matrix[new_r][new_y] == "1":
                dfs(new_r, new_y)
        return

    results = 0

    for r in range(m):
        for c in range(n):
            if not seen[r][c] and matrix[r][c] == "1":
                dfs(r, c)
                results += 1
    return results

validate(islands, inputs, outputs)