# Defining a function to add 2 numbers

def pud_sum(num1, num2):
    print(num1+num2)

print("Result:")
pud_sum(11,2)

# Assigning default values to parameters

def pud_add(numb1,numb2=4): # numb2 is asigned with value 4
    print(numb1+numb2)

print("Default value function:")
pud_add(2) # numb2 is automatically taken as 4 (default value)
