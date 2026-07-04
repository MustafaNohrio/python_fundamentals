#passing a function as an argument into another function
def square(num):
    return num * num

def operate(num, function):     #taking a function as parameter
    return function(num)        #square(num)
#operate() is a higher order function because it is accepting another function
value = 5
result = operate(value, square)     #pass value and function as argument
print(result)