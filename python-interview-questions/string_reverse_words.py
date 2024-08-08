from helpers.test import validate

inputs = [
    "Hello world",
    "The quick brown fox",
    "I love coding challenges"
]

outputs = [
    "olleH dlrow",
    "ehT kciuq nworb xof",
    "I evol gnidoc segnellahc"
]

def reverse_words(sentence):
    start = 0
    end = 0
    sentence_array = list(sentence)
    while end < len(sentence):
        if sentence[end] == " " or end == len(sentence) - 1:
            temp_start = start
            temp_end = end - 1 if sentence[end] == " " else end
            while temp_start < temp_end:
               temp_end_char = sentence_array[temp_end]
               sentence_array[temp_end] = sentence_array[temp_start]
               sentence_array[temp_start] = temp_end_char
               temp_start += 1
               temp_end -= 1
            end += 1
            start = end
        else:
            end += 1
    return "".join(sentence_array)

validate(reverse_words, inputs, outputs)
