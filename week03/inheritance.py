class employee:     #parent class
    company = 'NohrioAI'    #class variable
    PKR = 278
    AED = 3.67

    def __init__(self, first, last, pay):     
        self.first = first    
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com' 

    def greet(self):
        print('Hi, Welcome to the company', self.first, self.last)

    def change_currency(self):
        self.pay = int(self.pay * self.PKR) 
    

class developer(employee):  #child class >inheriting the attributes and behaviors(nethods) of parent class
    
    #init method of developer class
    def __init__(self, first, last, pay, prog_lang):    #extra variable prog_lang for developer class
        super().__init__(first, last, pay)    #instead of writing the same code for the variables of parent class doing this
        # employee.__init__(self, first, last, pay)   #Altrnative of super()
        #initializing the extra variable
        self.prog_lang = prog_lang
    
    def change_currency(self):
        self.pay = int(self.pay * self.AED)


class manager(employee):  #inheriting the employee class
    
    #init method of manger class
    def __init__(self, first, last, pay, employees=None):  #extra parameter >employees list supervised by manager 
        super().__init__(first, last, pay)   
        #when employee is passed as argument
        if employees is None:
            self.employees = [] #creating empty list
        else:
            self.employees = employees  #adding employee to 'employees' list
        
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)  #adding employee in the list when method is called

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)  #deleting employee from the list when method is called

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.first, emp.last)
    
emp_1 = employee('Mustafa', 'Nohrio', 50000)      
dev_1 = developer('Hamza', 'Arain', 70000, 'Python')  
dev_2 = developer('Mirani', 'Speaking', 60000, 'Java')  
mgr_1 = manager('Sajad', 'Soomro', 4000, [emp_1])    #giving emp_1 as arg

print('Employee 1 pay before: ', emp_1.pay)
emp_1.change_currency()
print('Employee 1 pay before: ', emp_1.pay)

#dev_1 is a developer but it can access the methods of employee class
print(dev_1.greet())
#when method is called python searches it in child class if not found then in parent class: MRO method resolution order
print('Employee 2 pay before: ', dev_1.pay) #developer
emp_1.change_currency()     #method of developer(child) is called
print('Employee 2 pay before: ', dev_1.pay)

print(dev_2.email)  #using innit method of parent class(employee)
print(dev_2.prog_lang)  #using innit method of child class(developer)

print(mgr_1.print_emp())    #--> Mustafa Nohrio
mgr_1.add_emp(dev_1)    #adding to the list
mgr_1.add_emp(dev_2)
print(mgr_1.print_emp())    #--> Mustafa Nohrio
                            #--> Hamza Arain
                            #--> Mirani Speaking 
mgr_1.remove_emp(emp_1) #removing from list
print(mgr_1.print_emp())    #--> Hamza Arain
                            #--> Mirani Speaking 
