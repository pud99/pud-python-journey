# This is a classic rock, paper, scissor game with scoreboard.

import random

# Scores are initially zero
computer_score = 0
user_score = 0
draws = 0
leading_points = 0 # This variable holds difference points

options = ["rock", "paper", "scissors"]

# Run an endless "while" loop till user quits.
while True:
    user_pick = input("Choose an option: rock, paper, scissors or press Q to quit\n").lower()

    if user_pick in options:
        print("Your choice", user_pick)

    elif user_pick == "q":
        print("Bye!")
        break

    else:
        print("Wrong option!")
        continue

    # 0: rock, 1: Paper, 2: scissor
    random_int = random.randint(0,2)
    computer_pick = options[random_int]

# If user and computer chooses same option

    if computer_pick == user_pick:
        draws +=1
        print("It's a draw, no points!")
        continue

    # Winning scenarios for player

    elif computer_pick == "rock" and user_pick == "paper":
        user_score += 1
        print("Computer picked:",computer_pick,". You win!")
        continue

    elif computer_pick == "paper" and user_pick == "scissors":
        user_score += 1
        print("Computer picked:",computer_pick,". You win!")
        continue

    elif computer_pick == "scissors" and user_pick == "rock":
        user_score += 1
        print("Computer picked:",computer_pick,". You win!")
        continue

    else:
        computer_score += 1
        print("Oops! you lost as computer picked:",computer_pick)
        continue

# Print score board

print("Your score:",user_score)
print("Computer score:", computer_score)

# Calculate leading points

if computer_score == user_score:
    print("The league is a draw between you and computer")

elif computer_score > user_score:
    leading_points = computer_score-user_score
    print("Computer won the league by", leading_points, "points.")

else:
    leading_points = user_score-computer_score
    print("You won the league by", leading_points, "points")
