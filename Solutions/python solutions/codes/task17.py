def countdown():
    count = 5
    if count > 0:
        while count > 0:
            print(count)
            count -= 1
    else:
        print("Invalid count value")

countdown()