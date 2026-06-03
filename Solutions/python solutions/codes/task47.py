def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError("Invalid operator.")

def main():
    try:
        a_str = input("Enter first number: ")
        a = float(a_str)
        b_str = input("Enter second number: ")
        b = float(b_str)
        op = input("Enter operator (+, -, *, /): ")
        result = calculate(a, b, op)
        print(f"Result: {a} {op} {b} = {result}")
    except ValueError as e:
        print(f"Error: Invalid input! {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
