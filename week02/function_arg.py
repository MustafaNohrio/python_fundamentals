def add (num1 = 0, num2 = 0):   #default arguments 
    return num1 + num2

result1 = add()
print(result1)      #0  >no error for empty arguments because of default arguments
result2 = add(6)
print(result2)      #6  >one argument is given other is default
result3 = add(6, 4)  #10  >both arguments are provided so no defalt argument is used
print(result3)
# result4 = add(3, 5, 7)   #gives error for using an extra argument
# print(result4)

def add (num1 , num2 , num3):   
    return num1 + num2 + num3 

result7 = add(5, 4, 3)
print(result7)


# *args
def add1(num1, *num2):      #variable length argument *num2 can take muliple arguments an save them as a tuple
    sum = num1
    for n in num2:
        sum += n
    return sum

addition = add1(3, 5, 8, 8, 4, 3)
print(addition)

#keyword arguments
def person(name, age):
    print('name: ', name)
    print('age: ', age)

person('Mustafa', 21)  #name:  Mustafa
                        #age:  21
person(21, 'Mustafa')   #name:  21
                        #age:  Mustafa
person(age=21, name='Mustafa')     #keyword arguments                 


#keywords length arguments (**kargs)
def person1(name, **kargs):
    print('name: ', name)
    print(kargs)     #{'age': 20, 'location': 'Karachi', 'tech': ' python'}
                    # **kargs save key-value pairs in a dctionary
    #accessing individual elements
    for k, v in kargs.items():
        print(k,' : ', v)

person1(name = 'Mustafa', age = 20, location = 'Karachi', tech = ' python')