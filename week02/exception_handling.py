# print(10 / 0)   #ZeroDivisionError: division by zero >program crashed
# print('Exeuted completely')   #this line is not printted

#with exception handaling the code will not crash due to errors it will continue execution
try:
    print(10 / 0)
except ZeroDivisionError:
    print('Cannot divide by zero')
print('Exeuted completely')

# #valueError
# n = int(input('Enter a number '))
# print(n)  
# print('Exeuted completely')  #this line is not executed when entered 'h' 
                            #"ValueError: invalid literal for int() with base 10: 'h'"

try:
    n = int(input('Enter a number '))
    print(n)
except ValueError:
    print('Invalid value entered')
print('Exeuted completely') #This line is executed regadlesss of the entered value


#general exception
try:
    print(10 / 0)
except Exception as e:
    print('Error occured:', e)  #Error occured: division by zero
print('Exeuted completely')

#Raising your own error
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")