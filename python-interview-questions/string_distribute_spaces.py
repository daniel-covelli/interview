from helpers.test import validate
import math

inputs = [
    [["There", "is", "a", "place", "that", "is", "big", "and", "large."], 11],
    [["When", "we", "cease", "to", "understand", "all."], 8],
    [["A", "professor", "apple", "tank", "teal", "world."], 16]
]

def build_spaces_array(words_length, length, number_of_words):
    spaces_array = []
    remaining_spaces = length - words_length
    space_strings_to_calculate = number_of_words - 1
    if not space_strings_to_calculate:
        return [""]
    spaces_per_word = remaining_spaces / space_strings_to_calculate
    for i in range(space_strings_to_calculate):
        if i == space_strings_to_calculate - 1:
             spaces_array.append(" " * math.floor(spaces_per_word))
        else:
            spaces_array.append(" " * math.ceil(spaces_per_word))
    spaces_array.append("")
    return spaces_array

def condense(line_words):
    addition_with_no_spaces = ""
    for word in line_words:
        addition_with_no_spaces += word
    return addition_with_no_spaces


def build_result_addition(line_words, length):
    spaces_array = build_spaces_array(len(condense(line_words)), length, len(line_words))
    result = ""
    for i in range(len(line_words)):
        result += line_words[i] + spaces_array[i]
    return result

def build_last_line(line, length):
    remaining_spaces = length - len(line)
    return line + " " * remaining_spaces

def distribute_spaces(words, length):
    results = []
    line = ""
    line_words = []
    for word in words:
        candidate = line + " " + word if line != "" else word
        if len(candidate) > length:
            results.append(build_result_addition(line_words, length))
            line = word
            line_words = [word]
        else:
            line = candidate
            line_words.append(word)
    results.append(build_last_line(line, length))
    return results

outputs = [
    [
        "There  is a",
        "place  that",
        "is  big and",
        "large.     "
    ],
    [
        "When  we",
        "cease to",
        "understand",
        "all.    "
    ],
    [
        "A      professor",
        "apple  tank teal",
        "world.          "
    ]
]

validate(distribute_spaces, inputs, outputs)