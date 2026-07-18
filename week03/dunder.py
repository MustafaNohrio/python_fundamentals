# Dunder(double underscore) methods allows us to change some builtin behaviors
class Employee:

    def __init__(self, first, last, pay):   #most common dunder method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@mail.com'

    def __repr__(self): #for developers and debugging
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):  #for users
        return '{}{} - {}'.format(self.first, self.last, self.email)

    def __add__(self, other):   #two objects
        return self.pay + other.pay

    def __len__(self):
        return len(self.first + self.last)

emp1 = Employee("Mustafa", "Nohrio", 50000)
emp2 = Employee("Ali", "Khan", 60000)

print(emp1) #MustafaNohrio - Mustafa.Nohrio@mail.com
print(emp1.__str__()) #MustafaNohrio - Mustafa.Nohrio@mail.com
print(emp1.__repr__()) #Employee('Mustafa', 'Nohrio', '50000')


#dunder add
 
# print(1 + 2)    #3 >add
# print(int.__add__(1 , 2))   #3
# print('1' + '2')    #12 >concates
# print(str.__add__('1' , '2'))   #12

print(emp1 + emp2)  #110000 >combined salaries

# len
print(len('Mustafa'))   #7
print('Mustafa'.__len__())  #7 >same

#dunder len
print(emp1.__len__())   #13