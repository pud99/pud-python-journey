marks = (99, 102, 35, 55, 55, 55)

# Count frequency of number in a tuple
print (marks.count(35))

# Index of a number inside tuple
print(marks.index(55))

# Iterate values inside tuple using for loop
for score in marks:
    print(score)

# Defining tuple without braces
users = "Cupcake", "Donut", "Puchku"
print(users)

# Notes
    # Tuples are immutable i.e you can't modify a tuple once defined
    # There is no need to assign brackets '()', even if skipped, it's considered as a tuple
      #Example: users = Cupcake, Donut, Puchku
