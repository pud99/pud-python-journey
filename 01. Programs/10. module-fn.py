# import math
# from math import *
# Print all functions from math
#print(dir(math))

# import only sqrt function from math
from math import sqrt
sqrt_value = input ("Which number square root would you like to calculate?\n")
# Convert the user input to int and then calculate
res = sqrt(int(sqrt_value))

# Convert values to string
res_str = str(res)
sqrt_value_str = str(sqrt_value)

print("Square root of "+sqrt_value_str+" = "+res_str)

