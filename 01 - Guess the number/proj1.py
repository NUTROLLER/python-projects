#Generate random number (target)
#let user guess value
#if correct --> game ends
#if lesser --> print lesser
#if more --> print more
import random
target = random.randint(1,100)
count = 0
while (True):
    guess = int(input("Enter guess (1-100) or Quit(0): "))
    if (guess == target):
        print("You have guessed the number!")
        print(f"Attempts: {count}")
        if count>10:
            print("You can do a lot better!")
        elif count<6: 
            print("You did excellent!")
        else:
            print("You can do better!")
        break
    elif (guess > target):
        print("Your guess is a little big. Try lower!")
        count+=1
    
    elif (guess<0 or guess>100):
        print("Please guess within 1 and 100")
        count+=1
    elif (guess == 0):
        print("Exiting...")
        break
    else:
        print("Your guess is a little small. Try higher!")
        count+=1

        