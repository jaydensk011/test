from random import randint

bot_rps = ["Rock", "Paper", "Scissors"]

try:
    user_rps = input("Rock, Paper or Scissors? ").capitalize()

    if user_rps not in bot_rps:
        print("Only input 'Rock', 'Paper', or 'Scissors'.")
    else:
        bot_rps_ = bot_rps[randint(0, 2)]

        if bot_rps_ == "Rock":
            if user_rps == "Rock":
                print("I picked rock, and you picked rock. It's a tie.")
            elif user_rps == "Paper":
                print("I picked rock, and you picked paper. You win!")
            elif user_rps == "Scissors":
                print("I picked rock, and you picked scissors. You lost.")

        elif bot_rps_ == "Paper":
            if user_rps == "Rock":
                print("I picked paper, and you picked rock. You lost.")
            elif user_rps == "Paper":
                print("I picked paper, and you picked paper. It's a tie.")
            elif user_rps == "Scissors":
                print("I picked paper, and you picked scissors. You win!")

        elif bot_rps_ == "Scissors":
            if user_rps == "Rock":
                print("I picked scissors, and you picked rock. You win!")
            elif user_rps == "Paper":
                print("I picked scissors, and you picked paper. You lost.")
            elif user_rps == "Scissors":
                print("I picked scissors, and you picked scissors. It's a tie.")

except Exception as e:
    print("An error occurred:", e)
