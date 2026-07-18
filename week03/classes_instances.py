class employee: #creating a class
    pass

emp_1 = employee()      #objects of the class
emp_2 = employee()

print(emp_1)    #<__main__.employee object at 0x0000028AA6146A50>

#initializing objects manually
emp_1.first = 'Mustafa'
emp_1.last = 'Nohrio'
emp_1.email = 'Mustafa.Nohrio@email.com'
emp_1.pay = 50000

emp_2.first = 'Hamza'
emp_2.last = 'Arain'
emp_2.email = 'Hamza.Arain@email.com'
emp_2.pay = 70000

#printing the object variables
print(emp_1.first)  #Mustafa
print(emp_1.pay)    #50000
print(emp_2.email)  #Hamza.Arain@email.com