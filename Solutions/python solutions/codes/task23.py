import math
def calculate_area(radius):
    if radius <= 0:
        print("Invalid radius! Radius must be greater than 0.")
        return
    area = math.pi * (radius ** 2)
    print(f"Area of Circle: {area:.2f}")
    return area
calculate_area(5)