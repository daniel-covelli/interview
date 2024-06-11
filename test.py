def validate(f, inputs, outputs):

    for i in range(len(inputs)):
        result = f(inputs[i])
        expected = outputs[i]
        if result != expected:
            print({"result": result, "expected": expected, "message": "Result not equal to expected"})
            break
        print("Test case " + str(i) + " has passed")