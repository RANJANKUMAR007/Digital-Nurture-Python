def next_year_age(age):

    if age.isdigit():
        age = int(age)
        print(f"Next year you'll be {age + 1}")
    else:
        print("Please enter a valid numeric age.")
a = input("Enter your age: ")
next_year_age(a)