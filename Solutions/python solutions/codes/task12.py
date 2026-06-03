def check_result():
    marks = input("Enter your marks: ")

    if marks.isdigit():
        marks = int(marks)

        if marks >= 35:
            print("Pass")
        else:
            print("Fail")
    else:
        print("Please enter valid marks.")

check_result()