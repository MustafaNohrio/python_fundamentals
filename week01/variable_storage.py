a = 5
b = 5
#a/b are variable names(references) and 5 is value stored in memory block
print(id(a))
print(id(b)) #a and b have same reference(both are pointing to the same memeory location)

c = 6
d = 7
print(id(c))
print(id(d)) #c and d have different reference(both are pointing to the different memeory location)


