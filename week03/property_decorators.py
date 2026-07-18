class Employee:

    def __init__(self, first, last, pay):   
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + '.' + last +'@mail.com'

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    #setting 'first' and 'last'
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')   #split name into first and last with given space
        self.first = first
        self.last = last

    
    #deleting 'first' and 'last'
    @fullname.deleter
    def fullname(self):
        print('Deleting name...')
        self.first = None
        self.last = None


emp1 = Employee("Mustafa", "Nohrio", 50000)
emp2 = Employee("Ali", "Khan", 60000)

print(emp1.first)   #Mustafa
print(emp1.email)   #Mustafa.Nohrio@mail.com
# print(emp1.fullname())  #Mustafa Nohrio
#after adding property decorator can access fullname() as an attribute 
print(emp1.fullname)    #Mustafa Nohrio

#changing first
emp1.first = 'Sajjid'
# print(emp1.first)   #Sajjid
# print(emp1.email)   #Mustafa.Nohrio@mail.com  >>did not change here
# print(emp1.fullname())  #Sajjid Nohrio
# #after creating separate mehod for email
# print(emp1.email())   #Sajjid.Nohrio@email.com  

#after adding property decorator can access email() as an attribute 
print(emp1.email)   #Sajjid.Nohrio@email.com
#after adding property decorator can access fullname() as an attribute 
print(emp1.fullname)   #Sajjid Nohrio

#want to set fullname and reflect those changes in 'fist' 'last' and 'email' as well >>using setter
emp1.fullname = 'Ghulam Mustafa'
print(emp1.email)   #Ghulam.Mustafa@email.com
print(emp1.fullname)    #Ghulam Mustafa]

#deleting name
del emp1.fullname
print(emp1.first)   #None