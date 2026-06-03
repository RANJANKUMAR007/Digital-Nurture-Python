def display_coordinates(coords):
    x, y = coords
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        print("Invalid coordinates")
        return
    print(f"X Coordinate: {x:.2f}")
    print(f"Y Coordinate: {y:.2f}")
point = (10.5, 20.8)
display_coordinates(point)