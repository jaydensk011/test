def password_function(poopybutt):
    password = "password"
    x = 0
    x = int(x)
    z = input("Guess the password: ")
    #if they guess wrong
    while(z != password and x<3):
        x = x+1
        print("the password you have inputted is incorrect")
        z = input("Guess the password: ")
    if (z != password):
        print("Locked out of account")
    else:
        print("Correct, welcome " + poopybutt.title())

def main():
    z = input("Give me your cool awesomesauce name: ")
    password_function(z)

if __name__ == "__main__":
    main()
