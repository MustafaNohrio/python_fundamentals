tup = 24, 65, 78, 44
print(type(tup))    #tuple

tup = (24, 65, 78, 44)
print(type(tup))    #this is also tuple

#Immutable
print(tup[2])   #78
# tup[2] = 55     #it will give error , cannot change


print(max(tup))     #78
print(min(tup))     #24
print(len(tup))     #4
print(24 in tup)    #True
#tuple with mixed values
tupA = (2, 'mustafa', 2.5)
print(tupA)     #(2, 'mustafa', 2.5)

#unpacking of a tuple
num, name, num2 = tupA
print(num)  #2
print(name)  #mustafa
print(num2)  #2.5

# num, name, num2, num3 = tupA       #Not enough values to unpack

#list in a tuple
tupB = (2, 'mustafa', [2, 3, 4, 5])
# tupB[2] = [6, 7, 8, 9]  #cannot change > immutable
# We can change the values inside of a list
tupB[2][0] = 9
print(tupB[2])  # [9, 3, 4, 5] value relaced because list is mutable
