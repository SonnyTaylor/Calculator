# Get user details and required inputs
name = input('Please enter your name: ')
try:
    age = int(input('Please enter your age: '))
except ValueError:
    print('Invalid age. Please enter a valid integer.')

# Depending on age print specific message
if age >= 100:
    print('Wow you are pretty old, Welcome!')
elif age < 2:
    print('Are you able to read? You seem too young!')
elif age <= 19:
    print("You're a teenager!")
elif age > 30:
    print("You're an adult!")
    print("You've reached a significant milestone in life!")
else:
    print("You're somewhere between a child and an adult!")

operation = input('Please enter an arithmetic operation (+, -, *, /): ')  # ask for arithmetic operation

try:
    num1 = int(input('What is your first number: '))  # ask for first number
    num2 = int(input('What is your second number: '))  # ask for second number

    if operation == '+':
        result = num1 + num2
        print(f'The sum of {num1} + {num2} = {result}')  # plus the 2 numbers together
    elif operation == '-':
        result = num1 - num2
        print(f'The difference of {num1} - {num2} = {result}')  # minus the 2 numbers
    elif operation == '*':
        result = num1 * num2
        print(f'The product of {num1} * {num2} = {result}')  # times the 2 numbers
    elif operation == '/':
        result = num1 / num2
        print(f'The division of {num1} / {num2} = {result}')  # divide the 2 numbers
    else:
        print('Invalid arithmetic operation')  # if input is not arithmetic operation print invalid operation
except ValueError:
    print('Invalid number input. Please enter valid integers for the numbers.')
