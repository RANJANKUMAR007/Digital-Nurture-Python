def login():
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    if user != "" and pwd != "":
        if user == "admin":
            if pwd == "pass123":
                print("Login Successful")
            else:
                print("Incorrect Password")
        else:
            print("Invalid Username")
    else:
        print("Username and Password cannot be empty")
login()