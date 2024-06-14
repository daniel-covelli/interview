from helpers.test import validate
from collections import deque

events = [
    {"type": "User", "metadata": {"location": "LA", "action": "Login", "status": "Success", "origin": "Home", "device": "Web"}},
    {"type": "Event", "metadata": {"location": "SF", "action": "Signup", "status": "Failure", "month": "March"}},
    {"type": "Event", "metadata": {"location": "NY", "action": "Signup", "status": "Success", "origin": "Dashboard", "device": "Mobile"}},
    {"type": "User", "metadata": {"location": "NY", "action": "Login", "status": "Failure", "origin": "Home", "device": "Mobile"}},
    {"type": "Event", "metadata": {"location": "SF", "action": "Login", "status": "Failure", "month": "March"}},
    {"type": "Event", "metadata": {"location": "SF", "action": "Signup", "status": "Success", "origin": "Dashboard", "device": "Mobile"}},
    {"type": "User", "metadata": {"location": "LA", "action": "Login", "status": "Failure", "origin": "Profile", "device": "Web"}},
    {"type": "Event", "metadata": {"location": "LA", "action": "Signup", "status": "Failure", "month": "September", "origin": "Profile", "device": "Web"}},
    {"type": "Event", "metadata": {"location": "NY", "action": "Login", "status": "Success", "origin": "Dashboard", "device": "Web"}}
]


def count(events, arguments):
    result = dict({})
    def recurse(vals, dict):
        if len(vals) == 1:
            if vals[0] in dict:
                dict[vals[0]] += 1
            else:
                dict[vals[0]] = 1
            return
        curr = vals.popleft()
        if curr in dict:
            recurse(vals, dict[curr])
        else:
            dict[curr] = {}
            recurse(vals, dict[curr])

    for event in events:
        vals = []
        for arg in arguments:
            if arg == "type":
                vals.append(event[arg])
            elif arg in event["metadata"]:
                vals.append(event["metadata"][arg])
        if len(vals) == len(arguments):
            recurse(deque(vals), result)
    return result

inputs = [[events, ["location"]], [events, ["action", "status", "device"]], [events, ["status", "location"]], [events, ["type", "action"]]]


outputs = [
    {"LA": 3, "NY": 3, "SF": 3},
    {
        "Login": {
            "Success": {
                "Web": 2,
            },
            "Failure": {
                "Web": 1,
                "Mobile": 1
            }
        },
        "Signup": {
            "Success": {
                "Mobile": 2
            },
            "Failure": {
               "Web": 1,
            }
        }
    },
    {
        "Success": {
            "LA": 1,
            "NY": 2,
            "SF": 1
        },
        "Failure": {
            "LA": 2,
            "NY": 1,
            "SF": 2
        }
    },
    {
        "Event": {
           "Login": 2,
           "Signup": 4
        },
        "User": {
            "Login": 3,
        }
    }
]

validate(count, inputs, outputs)