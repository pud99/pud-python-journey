# This is a game that lets the player guess the number.
# This program uses "random" module to generate random numbers

import random

"""
r = random.randint(0, 10) # randint() prints number in the range from 0 to 10 (including 10)
print(r)
"""

upper_range = input("Input an upper bound limit: ")

if upper_range.isdigit(): # Check if the input is number (.isdigit)
    upper_range = int(upper_range) # If it's a digit then convert it to int

    if upper_range <= 0: # Input should be greater than 0
        print("Input a number greater than 0")
        quit()

else: # If the user input is not a number then quit
    print("Input a number only")
    quit()

random_number = random.randint(0,upper_range)

# Number of chances user takes to guess the number. Initially set it to 0.
guesses = 0

while True:
    guesses +=1 # increment no. of guesses everytime user fails
    user_guess = input("Guess the number: ")

# Check if the input is a digit

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Input numbers only")
        continue

    if user_guess == random_number:
        print("That's correct! you guessed in", guesses, "chances")
        break

# If "guessed number" is lower than random number then, ask user to guess a higher number -
# - else ask user to guess lower number

    elif user_guess < random_number:
        print("Choose a higher number")
        continue

    else:
        print("Choose a lower number")
        continue