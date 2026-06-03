def divide(a, b):
    try:
        # Divide two numbers
        result = a / b

        # Print result
        print("Result:", result)

    except ZeroDivisionError:
        # Handle division by zero
        print("Error: Cannot divide by zero")

divide(10, 2)
divide(10, 0)