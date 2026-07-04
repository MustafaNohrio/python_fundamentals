def addition(x, y):
    return x + y;

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('Cannot divide by zero!')

print('CALCULATOR')

try:
    num1 = int(input('Enter first number ')) 
    num2 = int(input('Enter second number ')) 
except ValueError:
    print('You entered invalid value')

try:
    n = int(input('''
    Enter:
    1 for addition,
    2 for subtraction,
    3 for multiplication and
    4 for division
    ''')) 
except ValueError:
    print('You entered invalid value, please enter a number (1 - 4)')

match n:
    case 1:
        result = addition(num1, num2)
        print('Sum', result)
    case 2:
        result = subtraction(num1, num2)
        print('Difference', result)
    case 3:
        result = multiplication(num1, num2)
        print('Product', result)
    case 4:
        result = division(num1, num2)
        print('division', result)
    case _:
        print('You entered invalid value, please enter a number (1 - 4)')