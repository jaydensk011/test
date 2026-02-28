#asking for user input
while True:
    z = input("Guess the password: ")
    z = str(z)
    #if they guess wrong
    if str(z) != "password":
        print("the password you have inputted is incorrect")
    #if they guess correct
    if str(z) == "password":
        print("password correct")
        break