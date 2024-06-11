
def validate(f, inputs, outputs):
    for i, input in enumerate(inputs):
        result = f(*input) if isinstance(input, list) else f(input)
        expected = outputs[i]
        if result != expected:
            print({"result": result, "expected": expected, "message": "Result not equal to expected"})
            raise Exception("Tests failing")
        print("Test case " + str(i) + " has passed")