#This program plays rock paper scissors with you! 
#Enter 'r' for rock, 'p' for paper, 's' for scissors and 'e' for exit...

import random
import time
def play_game():
    choices = ["rock", "paper", "scissors"]
    isPlaying = True
    while isPlaying:
        opp_choice = random.choice(choices)
        user = input("Rock(r), paper(p) or scissors(s)? [Enter 'e' to exit]:").lower().strip()
        if user not in ['r','p','s','e']:
            print("Oops! Please enter 'r', 'p' or 's' only!")
        else:
            if (user == 'e'):
                print("Exiting...")
                isPlaying = False
            elif (user == opp_choice[0]):
                time.sleep(0.5)
                print(f"Computer chose {opp_choice}!")
                print("It's a tie!")
            elif (user == 'r' and opp_choice == "scissors") or \
                 (user == 'p' and opp_choice == "rock") or \
                 (user == 's' and opp_choice == "paper"):
                    time.sleep(0.5)
                    print(f"Computer chose {opp_choice}!")
                    print("You win!")
            else:
                time.sleep(0.5)
                print(f"Computer chose {opp_choice}!")
                print("You lose")
play_game()


#Improvements and learnings:
# 
#  1. In rps, you only need to check winning/losing and tie conditions. The remaining
#     condition is automatically "else".
#  2.To check whether an input is = one in a certain list of characters
#    --> user_input in ['a', 'b', 'c'] --> Returns True if user_input is one of these...
#  3. Use a \ to split a long line of code into different lines
#