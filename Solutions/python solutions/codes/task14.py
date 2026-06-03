def assign_grade():
    score = input("Enter your score: ")
    if score.isdigit():
        score = int(score)
        if score >= 90:
            print("Grade: A")
        elif score >= 75:
            print("Grade: B")
        elif score >= 50:
            print("Grade: C")
        else:
            print("Grade: Fail")
    else:
        print("Please enter a valid score.")
assign_grade()