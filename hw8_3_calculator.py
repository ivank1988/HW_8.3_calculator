# Write a program that does the basic arithmetic operations:
# addition (+),
# subtraction (-),
# multiplication (*),
# and division (/).
# Ask the user to enter two numbers and the arithemtic operation ("+", "-", "*" or "/").
# Then use if/elif/else statements to do the right operation. A hint:
# if operation == "+":


first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
arithmetic_operation = input("Enter arithmetic operation (+),(-),(*) or (/): ")

if arithmetic_operation == "+":
    print(first_num + second_num)
elif arithmetic_operation == "-":
    print(first_num - second_num)
elif arithmetic_operation == "*":
    print(first_num * second_num)
elif arithmetic_operation == "/":
    print(first_num / second_num)
else:
    print("Try again, you entered wrong arithmetic operation")
