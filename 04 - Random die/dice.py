import random
import time
def roll():
    print("Now rolling dice...")
    time.sleep(0.5)
    outcome = random.randint(1,6)
    dice = {
        1:"⚀",
        2:"⚁",
        3:"⚂",
        4:"⚃",
        5:"⚄",
        6:"⚅"
    }
    print(dice[outcome])
roll()
while True:
    ask = input("Roll again? (y/n):").strip().lower()
    if (ask == 'y'):
        roll()
    elif(ask == 'n'):
        break
    else:
        print("Oops, please enter 'y' or 'n'!.")