import random

# generate a random number between 1 and 100(You can change the biger or samller number to guess)
number = random.randint(1, 100)

# set the number of guesses to 0(Don't edit)
guesses = 0

# loop until the user guesses the number or runs out of guesses
while guesses < 10:
    # ask the user to guess a number
    guess = int(input("Guess a number between 1 and 100: "))
    
    # increment the number of guesses
    guesses += 1
    
    # check if the guess is correct
    if guess == number:
        print("Congratulations, you guessed the number!")
        break
    elif guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
        
    # if the player has guessed 5 times and still hasn't won, print "Try again"
    if guesses == 5:
        print("Try again")
        
# if the user runs out of guesses, reveal the number
if guesses == 10:
    print("Sorry, you ran out of guesses. The number was", number)

#HMCLXOX(HugoXOX3)
