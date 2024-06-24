from helpers.test import validate
inputs = [1, 6, 15, 25]

def fibonacci(i):
    cache = dict()
    def recurse(i):
        if i in cache:
            return cache[i]
        if i == 0:
            return 0

        if i == 1:
            return 1

        result = fibonacci(i - 2) + fibonacci(i - 1)
        cache[i] = result
        return result
    return recurse(i)

outputs = [1,8, 610, 75_025]

validate(fibonacci, inputs, outputs)

