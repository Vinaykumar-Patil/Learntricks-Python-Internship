# Question [2]
'''Calculator: Build a basic calculator program that can perform arithmetic operations
(addition, subtraction, multiplication, division) based on user input.'''

first = input("Enter first number : ")
second = input("Enter second number : ")
first = int(first)
second = int(second)
print("----press keys for operator (+,-,*,/,%)----------") 
operator = input("Enter operator : ")
if operator == "+" :
	print(first + second)
elif operator == "-" :
	print(first - second)
elif operator == "*" :
	print(first * second)
elif operator == "/" :
	print(first / second)
elif operator == "%" :
	print(first % second)
else:
	 print("Invalid Operation") 


# Using 'eval' library
print(eval(input("Enter your calculation :")))
