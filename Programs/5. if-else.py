# This program checks the age for voting rights

age = input("What is your age? \n")
age = int(age)

if age >= 18:
    print("You can vote!")

elif age < 18 and age > 3:
    print("Hey, you're a school kid!")

else:
    print("Sorry, you can't vote")

print("Thank you for your time")