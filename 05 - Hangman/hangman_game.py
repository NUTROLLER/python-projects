import random

words = ["apple", "banana", "tiger", "house", "chair",
         "laptop", "python", "school", "galaxy", "thunder",
         "nightmare", "triangle", "spacecraft", "velocity", "algorithm"]

word = random.choice(words)
word_len = len(word)

print("Word has been picked!")
print(f"Your word contains {word_len} letters!")

word_letters = list(word)

found = False #Turn this true when word is found & exit the loop.
attempts = 0 #No of user attempts
max_attempts = 10

display_word = [] #contains underscores, later revealed by words!
for char in word_letters:
    display_word.append("_")

while (attempts < max_attempts):
    print(display_word)
    guess = input("Guess: ").lower().strip()
    #More than one character entered case:
    if (len(guess) > 1):
        print("Please put one letter at a time!")
    #Match found case:
    elif (word.find(guess)!=(-1)):
        indices_of_guessed_words = [i for i, char in enumerate(word) if char == guess]
        no_of_repetitions = len(indices_of_guessed_words)
        i = 0 #to loop thru indices
        while (i<no_of_repetitions):
            display_word[indices_of_guessed_words[i]] = guess;
            i+=1
        print(f"{guess} belongs in the word!")
        #Check each time whether the word has been found or not
        #If found, exit with a indicator variable "Found"
        if (display_word == word_letters):
            found = True
            break
        else: 
            pass
    #Match not found case:
    else:
        attempts+=1
        print(f"{guess} is not in the word! Try something else...")
        print(f"remaining attempts: {max_attempts-attempts}")

if (found):
    score = 1000 - (attempts*100)
    print(f"\nCongratulations! You found the word!!!\nThe word was: {word}.\nNumber of guesses: {attempts}\nScore: {score}\n")
else:
    print(f"\nUh oh, you were unable to find the word :(\nThe word was: {word}\nWhy don't you try again?")