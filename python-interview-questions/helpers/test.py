
def validate(f, inputs, outputs):
    for i, input in enumerate(inputs):
        result = f(*input) if isinstance(input, list) else f(input)
        expected = outputs[i]
        if result != expected:
            print({"result": result, "expected": expected, "message": "Result not equal to expected"})
            raise Exception("Tests failing")
        print("Test case " + str(i) + " has passed")


def runAllTests(tests):
    for test in tests:
        test()

def expect(testName, expected, actual):
    print("Running: " + testName)
    if expected == actual:
        print("Test passed, expected " + str(expected) + " equaled " + str(actual))
        print("\n")
    else:
        print("Test failed, Expected " + str(expected) + " did not equal actual " + str(actual))
        raise Exception("Test failed :(")