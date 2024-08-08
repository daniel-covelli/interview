from helpers.test import validate

inputs = [
    {
        "a": "1",
        "b": {
            "c": "2",
            "d": {
                "e": "3"
            }
        },
        "f": "4"
    },
    {
        "a": {
            "b.c": {
                "d": "1"
            },
            "b": {
                "c.d": "2"
            }
        },
        "a.b.c.d": "3",
        "": {
            "e": "4"
        },
        "f.": {
            ".g": {
                "..h": "5"
            }
        }
    },
    {
        "a": {
            "b": "1",
            "c": "2",
            "f": {
                "g": {
                    "z": "100"
                }
            }
        },
        "a.b": "3",
        "a.c": "4"
    }
]

outputs = [
    {
        "a": "1",
        "b.c": "2",
        "b.d.e": "3",
        "f": "4"
    },
    {
        "a.b.c.d": "1",
        "a.b.c.d_2": "2",
        "a.b.c.d_3": "3",
        ".e": "4",
        "f...g...h": "5"
    },
    {
        "a.b": "1",
        "a.c": "2",
        "a.b_2": "3",
        "a.f.g.z": "100",
        "a.c_2": "4",
    }
]




def flatten_easy(dictionary):
    result = {}
    suffixes = {}
    def extract(preface, dictionary):
        for key in dictionary.keys():
            if isinstance(dictionary[key], dict):
                extract(preface + key + ".", dictionary[key])
            else:
                if preface + key in result:
                    if preface + key not in suffixes:
                        suffixes[preface + key] = 2
                    else:
                        suffixes[preface + key] = suffixes[preface + key] + 1
                    result[preface + key + "_" + str(suffixes[preface + key])] = dictionary[key]
                else:
                    result[preface + key] = dictionary[key]
    extract("", dictionary)
    return result


validate(flatten_easy, inputs, outputs)