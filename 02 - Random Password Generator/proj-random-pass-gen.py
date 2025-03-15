#Generate a completely random 'n' length password

#random.choice(choices, k=len) selects a random symbol from a given set of choices(string,tuple,list)
#and accepts k = length (how many random things to select)

#"separator".join() joins all elements (from a list, tuple or a string) into a single string
# using given separator. e.g "-".join(["Hello", "World"]) gives Hello-World

import random
import string
length = int(input("Enter length of password: "))
password =""
i = 0
letters = "$#@%_+!&"
while(i<length):
    rand = random.randint(0,2)
    if (rand==0):
        password += str(random.randint(0,9))
    elif (rand == 1):
        password += random.choice(letters)
    else:
        password += random.choice(string.ascii_letters)
    i+=1
print(password)
toStore = input("Do you want to save your password? (Y/N): ")
if (toStore == 'Y' or toStore == 'y'):
    with open("pass.txt", "a") as f:
        f.write(password)
        f.write("\n")
    print("Password stored.")

# Alternate method literally 3 lines

symbols = string.digits + string.ascii_letters + letters
passd2 = "".join(random.choices(symbols, k=length))
print(passd2)
