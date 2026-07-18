class Employee:

    #class varibles are inside the class and outside all the methods
    raise_amount = 1.05 #class variable

    def __init__(self, first, last, pay):
        #instance variables >unique for each object
        self.first = first
        self.last = last
        self.pay = pay

emp1 = Employee("Mustafa", "Nohrio", 50000)
emp2 = Employee("Ali", "Khan", 60000)

#class variables are shared by all objects because they actually belong to the class
print(emp1.raise_amount)    #1.05
print(emp2.raise_amount)    #1.05

#accessing through class
print(Employee.raise_amount)    #1.05

#changing a class variable
Employee.raise_amount = 1.10

print(Employee.raise_amount)    #1.1

#now every object sees thw same value
print(emp1.raise_amount)    #1.1
print(emp2.raise_amount)    #1.1

#changing it through one object
emp1.raise_amount = 1.20

print(emp1.raise_amount)    #1.2 >new instance variable created for emp1
print(emp2.raise_amount)    #1.1 >class variable
print(Employee.raise_amount)    #1.1 >class variable    