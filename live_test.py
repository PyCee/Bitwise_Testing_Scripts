bitwise_equation = input("Enter bitwise testing with placeholder 'x': ")
x = int(input("Enter binary input to run through the equation: 0b"), 2)
while True:
    results = eval(bitwise_equation)
    print("Result: " + format(results, '#010b') + "\n")
    print("Enter with no input to use results of last calculation")
    next_input = input("Enter binary input to run through the equation: 0b")
    if len(next_input) < 1:
        x = results
    else:
        x = int(next_input, 2)
