class employee: 
    company = 'NohrioAI'    #class variable

    def __init__(self, first, last, pay):     
        self.first = first    
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com' 

    #class method >takes class as parameter
    #used when working with class variables
    @classmethod   #decorator
    def company_info(cls):     #here cls reprsents the employee class
        return cls.company    #access class variable

    #instance method >takes self(object instance) as parameter
    #used when working with instance variables
    def greet(self):
        print('Hi, Welcome to the company', self.first, self.last)


    #static method >there to use extra featues
    def dollar_to_rupee(dollar):
        return dollar * 278
    
emp_1 = employee('Mustafa', 'Nohrio', 50000)      
emp_2 = employee('Hamza', 'Arain', 70000)   

print(employee.company_info())  #NohrioAI

print(emp_1.company_info())  #NohrioAI
print(emp_1.greet())  #Hi, Welcome to the company Mustafa Nohrio
print(employee.dollar_to_rupee(5000))   #1390000