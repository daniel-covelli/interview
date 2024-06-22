from helpers.test import validate

inputs = [
    [
        [
            [15,18],
            [1,3],
            [2,6],
            [8,10]
        ]
    ], [
        [
            [1,4],
            [4,5]
        ]
    ],
    [
        [
            [1,4],
            [2,3]
        ]
    ]
]

outputs = [
    [
        [1, 6],
        [8, 10],
        [15, 18]
    ],
    [
        [1,5]
    ],
    [
        [1,4]
    ]
]

def merge(intervals):
    sorted_intervals = sorted(intervals)
    results = []
    span = sorted_intervals[0]
    for i in range(1, len(intervals)):
        [current_left, current_right] = sorted_intervals[i]
        if current_left >= span[0] and current_left <= span[1]:
            if current_right < span[1]:
                continue
            span[1] = current_right
        else:
            results.append(span)
            span = sorted_intervals[i]

    results.append(span)
    return results

validate(merge, inputs, outputs)