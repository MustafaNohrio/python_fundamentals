a = 10  #global variable

def something():
    a = 15  #local variable
    print('Inside variable: ', a)  #15
    print(globals()['a'])       #10 accessing global variable
something() 

print('outside variable: ', a)  #10

#assign the value to global variable inside a function
b = 10  #global variable

def something():
    b = 15  #local variable
    print('Inside variable: ', b)  #15
    (globals()['b']) = 33      #assign the value to global variable
something() 

print('outside variable: ', b)  #33