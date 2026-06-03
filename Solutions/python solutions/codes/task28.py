def write_greeting():
    file = open("greeting.txt", "w")
    file.write("Hello World")
    file.close()
    print("Message written to file successfully")
write_greeting()