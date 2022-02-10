num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operator = input("Enter arithmetic operator (+, -, /, *, %) : ")

num1 = int(num1)
num2 = int (num2)
if operator == "+":
    result = num1+num2

elif operator == "-":
    result = num1-num2

elif operator == "*":
    result = num1*num2

elif operator == "/":
    result = num1/num2

elif operator == "%":
    result = num1%num2

else:
    print("Incorrect operator")

print(result)