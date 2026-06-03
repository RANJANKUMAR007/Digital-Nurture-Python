def greet_user(name):
    if name.strip() == "":
        print("Name cannot be empty")
    else:
        print(f"Hello, {name}! Welcome.")
name = input("Enter your name: ")
greet_user(name)
