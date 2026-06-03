def area(length, width):
    if length <= 0 or width <= 0:
        print("Invalid input")
        return
    return length * width
result = area(5, 3)
print("Area:", result)