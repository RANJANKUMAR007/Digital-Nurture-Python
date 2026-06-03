def display_coordinates(coords):
    # Validate input type
    if not isinstance(coords, tuple):
        print("Invalid input: Coordinates must be a tuple.")
        return
    if len(coords) != 2:
        print("Invalid input: Coordinates must contain exactly 2 values (x, y).")
        return
    x, y = coords
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        print("Invalid input: Coordinates must be numbers.")
        return
    print(f"Coordinates are: (X = {x}, Y = {y})")
point = (10, 25)

display_coordinates(point)