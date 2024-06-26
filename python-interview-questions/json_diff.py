from helpers.test import validate

def added(value):
    return {"added": value}

def removed(value):
    return {"removed": value}

def changed(old, new):
    return {"changed": {"old": old, "new": new}}

def list_diff(list1, list2):
    result = {}
    len1 = len(list1)
    len2 = len(list2)
    length = max(len1, len2)
    for i in range(length):
        if i > len1 - 1:
            result[str(i)] = added(list2[i])
        elif i > len2 - 1:
            result[str(i)] = removed(list1[i])
        elif list1[i] != list2[i]:
                result[str(i)] = changed(list1[i], list2[i])
    return result

def orderedSet(json1, json2):
    result = []
    seen = set()
    for x in list(json1.keys()) + list(json2.keys()):
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result

def json_diff(json1, json2):
    result = {}
    unique_keys = orderedSet(json1, json2)
    for key in unique_keys:
        if key in json1 and key not in json2:
            result[key] = removed(json1[key])
        elif key in json2 and key not in json1:
            result[key] = added(json2[key])
        elif isinstance(json1[key], dict) and isinstance(json2[key], dict):
            diff = json_diff(json1[key], json2[key])
            if diff:
                result[key] = diff
        elif isinstance(json1[key], list) and isinstance(json2[key], list):
            diff = list_diff(json1[key], json2[key])
            if diff:
                result[key] = diff
        elif json1[key] != json2[key]:
            result[key] = changed(json1[key], json2[key])
    return result

inputs = [
    [
        {
            "name": "John Doe",
            "age": 30,
            "address": {
                "street": "123 main st",
                "city": "Anytown",
                "zip": "12345"
            },
            "hobbies": ["reading", "cycling"]
        },
        {
            "name": "John Doe",
            "age": 31,
            "address": {
                "street": "456 Elm st",
                "city": "Anytown",
                "country": "USA"
            },
            "hobbies": ["reading", "swimming"],
            "job": "Engineer"
        }
    ],
    [
        {
            "a": 1,
            "b": {
                "c": 2,
                "d": [3, 4, 5]
            },
            "e": "old"
        },
        {
            "a": 1,
            "b": {
                "c": 2,
                "d": [3, 4, 6]
            },
            "f": "new"
        }
    ],
    [
        {
            "numbers": [1, 2]
        },
        {
            "numbers": [1, 2, 3]
        }
    ],
    [
        {
            "numbers": [1, 2]
        },
        {
            "numbers": [1, 2]
        }
    ],
    [
        {
            "user": {
                "name": "John",
                "age": 30
            }
        },
        {
            "user": "John Doe"
        }
    ]
]

outputs =[
    {
        "age": {
            "changed": {
                "old": 30,
                "new": 31
            }
        },
        "address": {
            "street": {
                "changed": {
                    "old": "123 main st",
                    "new": "456 Elm st"
                }
            },
            "zip": {
                "removed": "12345"
            },
            "country": {
                "added": "USA"
            }
        },
        "hobbies": {
            "1": {
                "changed": {
                    "old": "cycling",
                    "new": "swimming"
                }
            }
        },
        "job": {
            "added": "Engineer"
        }
    },
    {
        "b": {
            "d": {
                "2": {
                    "changed": {
                        "old": 5,
                        "new": 6
                    }
                }
            }
        },
        "e": {
            "removed": "old"
        },
        "f": {
            "added": "new"
        }
    },
    {
        "numbers": {
            "2": {
            "added": 3
            }
        }
    },
    {},
    {
        "user": {
            "changed": {
                "old": {
                    "name": "John",
                    "age": 30
                },
                "new": "John Doe"
            }
        }
    }
]



validate(json_diff, inputs, outputs)