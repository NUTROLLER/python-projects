import random
import time

def play():
    global k
    k = 0
    print("Welcome to Tic-Tac-Toe!")
    #Generate a 3x3 matrix
    t = [ ["_"]*3 for i in range(3)]
    global gameEnded
    gameEnded = False
    for i in t:
        print(i)
        #Input:
    toss = random.randint(0,1)
    user_character = str(input("Your choice (X or O): ")).upper().strip()
    if user_character not in ["X", "O"]:
        print("Oops! Please enter only X or O!")
    else:
        if (user_character == "X"):
            computer_character = "O"
        else:
            computer_character = "X"
    #If 1, then human plays first
            toss = random.randint(0, 1)
        if toss == 1:
            print("You play first!")
        else:
            print("Computer plays first!")
            computer_chooses(t, computer_character)
        while not gameEnded:
            if gameEnded:
                return
            #User's turn:
            userChoice(t, computer_character, user_character)

def userChoice(t, computer_character, user_character):
     user_input = int(input("Your choice(1-9)?:"))
     validated = False
     while not validated:
            if (user_input not in range(1,10)):
                print("Please choose within 1 to 9!")
            else:
                validated = True
                user_input -= 1
                print(f"You chose: {user_input+1}")
        #Check to make sure spaces are not taken
            taken = False
            if (user_input in range(0,3)):
                if t[0][user_input] in ["X", "O"]:
                    taken = True
            elif (user_input in range(3,6)):
                if t[1][user_input%3] in ["X", "O"]:
                   taken = True
            elif (user_input in range(6,9)):
                if t[2][user_input%3] in ["X", "O"]:
                   taken = True
            if (taken == True):
                print("That space is already taken! Choose again.")

            elif (taken == False):
                    if (user_input in range(0,3)):
                        t[0][user_input] = user_character;
                    elif (user_input in range(3,6)):
                        t[1][user_input%3] = user_character;
                    elif (user_input in range(6,9)):
                        t[2][user_input%3] = user_character;
                    for i in t:
                        print(i)
                    check_winner(t)
                    checkForTie(t)
            #Computer turn:
            if gameEnded:
                 return
            computer_chooses(t, computer_character)
            check_winner(t)
            checkForTie(t)

#Computer choosing function
def computer_chooses(t, computer_character):
                if gameEnded:
                     return
                computer_choice = random.choice(range(1,10))  
                computer_choice -=1
            #Check to make sure spaces are not taken
                taken = False
                if (computer_choice in range(0,3)):
                    if t[0][computer_choice] in ["X", "O"]:
                        taken = True
                elif (computer_choice in range(3,6)):
                    if t[1][computer_choice%3] in ["X", "O"]:
                        taken = True
                elif (computer_choice in range(6,9)):
                    if t[2][computer_choice%3] in ["X", "O"]:
                        taken = True
                if (taken == True):
                    computer_chooses(t, computer_character)
                else:
                    print(f"Computer choosing...")
                    time.sleep(0.5)
                    print(f"Computer chose: {computer_choice+1}")
                    if (computer_choice in range(0,3)):
                        t[0][computer_choice] = computer_character
                    elif (computer_choice in range(3,6)):
                        t[1][computer_choice%3] = computer_character
                    elif (computer_choice in range(6,9)):
                        t[2][computer_choice%3] = computer_character
                for i in t:
                    print(i)

#Check winner function
def check_winner(t):
                global k
                global gameEnded
                for k in range(3):
                    if (t[k][0] == t[k][1] == t[k][2] and t[k][0] != '_'):
                        gameEnded = True
                        print("Game ended!")
                        print(f"{t[k][0]} is the winner!")
                        return 
                    elif (t[0][k] == t[1][k] == t[2][k] and t[0][k] != '_'):
                        gameEnded = True
                        print("Game ended!")
                        print(f"{t[0][k]} is the winner!")
                        return 
                    #Check diagonals
                if (t[0][0] == t[1][1] == t[2][2] and t[0][0] != '_'):
                        gameEnded = True
                        print("Game ended!")
                        print(f"{t[0][0]} is the winner!")
                        return 
                elif (t[0][2] == t[1][1] == t[2][0] and t[0][2] != '_'):
                        gameEnded = True
                        print("Game ended!")
                        print(f"{t[0][2]} is the winner!")
                        return 

                #Return false if no winner found
                return False

def checkForTie(t):
    global gameEnded
    for k in range(3):
        for j in range(3):
            if t[k][j] == '_':
                return False  # If there's an empty space, it's not a tie
    print("It's a draw!")
    gameEnded = True
    return True
play()