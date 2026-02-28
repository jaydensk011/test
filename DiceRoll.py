import random
try:
    guess = int(input("What is the dice roll? "))
    if guess > 6 or guess < 1:
        print("You can only pick numbers from 1 to 6.")
    else: 
        diceroll = random.randint(1,6)
        if diceroll == guess:
            print("You guessed correctly! Congratulations!")
        else:
            diceroll = str(diceroll)
            print("You guessed incorrectly. The roll was " + diceroll + ".")
except ValueError:
    print("You can only enter numbers that are integers!")
