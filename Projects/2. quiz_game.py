# This is a quiz game using if-else statements and player will also get score after playing the game

# Greeting the player and asking name
player_name = input("What is your name?\n")
print("Hello "+player_name)

# Ask player if they want to play
player_decision = input("Would you like to play a simple quiz? yes/no\n")

# convert inputs to lower case
# player_decision = player_decision.lower()

# If player response is not 'yes', then we quit else we can continue
if(player_decision.lower() != "yes"):
    print("Bye "+player_name+"!")
    quit() # Quit program

# Continue program
print("Good choice, let's play! ")
score = 0 # Reset score to zero

# Question 1:
answer = input("What is the full form of CPU?\n")

if (answer.lower() == "central processing unit"):
    score = score+1
    print("That's correct!")
else:
    print("Oops! wrong answer.")

# Question 2:
answer = input("What is the full form of RAM?\n")

if (answer.lower() == "random access memory"):
    score = score + 1
    print("That's correct!")
else:
    print("Oops! wrong answer.")

# Question 3:
answer = input("What is the full form of ROM?\n")

if (answer.lower() == "read only memory"):
    score = score + 1
    print("That's correct!")
else:
    print("Oops! wrong answer.")

print("Your score is: "+str(score))
print("Percentage is: "+str((score/3)*100)+"%")