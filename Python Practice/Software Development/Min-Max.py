# read two numbers
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# choose the larger number
if number1 > number2:
    max = number1
else:
    max = number2

#print the result
print("The larger number is",max)