#list is a collection of values stored in a variable
num = [45, 55, 65, 75, 85, 95]
print(num)      #print all
print(num[0])   #print first
print(num[3])   #print fourth
print(num[-1])   #print last
# print(num[9])   #index out of bound

#slicing
print(num[1:5])   #second to fifth (index [5] is exclusive)
print(num[2:])     #third to last

#list of strings
names = ['mustafa', 'rizwan', 'hamza']
#list of mixed data types
items = ['mustafa', 55, 9.3]

#adding two lists in a single list
mix = [num , names]
len(mix)  #2
print(mix)
print(mix[0])   #[45, 55, 65, 75, 85, 95] as a sigle element
print(mix[0] [1])   #55

combine = [num + names]  #combines all as distinct elements
print(combine)

#Operations with functions on list
num = [45, 55, 65, 75, 85, 95]
num.append(33)  #adds at the end of the list
print(num)
num.insert(1,13)    #add element at specific index
print(num)
num.remove(55)    #remove specific element 
print(num)
num.pop()    #remove element from specific index
print(num)
del num[1:4]    #deleting a part
print(num)
num.extend([10, 20, 40])    #add at the end
print(num)
num[1:3] = [44, 45, 46]     #replace elements
print(num)

num.reverse()
print(num)
num.sort()
print(num)

print(num.count(45))   #count occurance of an element
print(num.index(45))    #find index of the element 

print(min(num))
print(max(num))
print(sum(num))
print(min(names))
