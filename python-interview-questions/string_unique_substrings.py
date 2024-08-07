from helpers.test import validate

inputs = [
    [
        [
            "Bird",
            "Cat",
            "Mouse",
            "Dog",
            "Cabfish"
        ]
    ],
    [
        [
            "Tird",
            "Cat",
            "Mouse",
            "Dog",
            "Catfish"
        ]
    ]
]

outputs = [
    [
        "Bi<u>r</u>d",
        "Ca<u>t</u>",
        "<u>M</u>ouse",
        "Do<u>g</u>",
        "Cab<u>f</u>ish"
    ],
    [
        "Ti<u>r</u>d",
        "Cat",
        "<u>M</u>ouse",
        "Do<u>g</u>",
        "Cat<u>f</u>ish"
    ]
]

def unique_character(words):
    sets = []
    for w in words:
        sets.append(set([c.lower() for c in w]))
    words_len = len(words)
    results = []
    for i in range(words_len):
        curr_word = words[i]
        for k in range(len(curr_word)):
            k_valid = True
            for j in range(words_len):
                if i == j:
                    continue
                if curr_word[k].lower() in sets[j]:
                    k_valid = False
                    break
            if k_valid:
                results.append(curr_word[:k] + "<u>" + curr_word[k] + "</u>" + curr_word[k + 1:])
                break
        if len(results) - 1 != i:
            results.append(curr_word)
    return results

validate(unique_character, inputs, outputs)
