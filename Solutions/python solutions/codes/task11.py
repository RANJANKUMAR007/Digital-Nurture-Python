def convert_weight():
    kg = input("Enter weight in kilograms: ")
    try:
        kg = float(kg)
        lbs = kg * 2.20462
        print(f"Weight in pounds: {lbs}")
    except ValueError:
        print("Please enter a valid decimal number.")
convert_weight()