def check_even_odd():
    num = input("Enter a number: ")

    if num.isdigit():
        num = int(num)

        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")
    else:
        print("Please enter a valid number.")

check_even_odd()