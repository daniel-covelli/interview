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
    ]
]

outputs = [
    [
        "Bi<u>r</u>d",
        "Ca<u>t</u>",
        "Mo<u>u</u>se"
        "Do<u>g</u>",
        "Cabfis<u>h</u>"
    ]
]

def unique_character(words):
    return []

validate(unique_character, inputs, outputs)
