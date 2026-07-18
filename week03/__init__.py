class employee: #creating a class
    def __init__(self, first, last, pay):     #special method recieves self as first parameter by default
        #setting instance variables >unique for each object
        self.first = first     #'self' is an instance (points to the current object) 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com' 

    def greet(self):
        print('Hi, Welcome to the company', self.first, self.last)

emp_1 = employee('Mustafa', 'Nohrio', 50000)      #objects of the class
emp_2 = employee('Hamza', 'Arain', 70000)   #__init__ method is called automaticaly when objects are created


#printing the object variables
print(emp_1.first)  #Mustafa
print(emp_1.pay)    #50000
print(emp_2.email)  #Hamza.Arain@email.com

#calling the method in the different ways tha means the same
emp_1.greet()   #Hi, Welcome to the company Mustafa Nohrio
employee.greet(emp_2)   #Hi, Welcome to the company Hamza Arain
