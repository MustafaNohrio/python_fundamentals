from array import *

arr = array('i', [34, 45,6, 56])    # i > signed int
print(arr)      #array('i', [34, 45, 6, 56])

print(arr.buffer_info())    #(2583786554016, 4)  >address and size

#iteraion
for i in arr:
    print(i)

print(arr.tolist()) # converting to list >[34, 45, 6, 56]

#functions of array
arr.append(66)  #Add 66 at the end
print(arr)

arr.reverse()    #reverse aray
print(arr)

arr1 = arr  #copying array
print(arr)
print(arr1)

arr1[2] = 55    #changging value of one array
print(arr)  #array('i', [66, 56, 55, 45, 34])
print(arr1) #array('i', [66, 56, 55, 45, 34])
#both arrays have 55 at index 2 because we have two varibles refering to the same array

#creating the same array with different reference
arr1 = array('i', arr.tolist())
print(arr)
print(arr1)
#now changing the value of one array will not affact the other
arr1[2] = 11
print(arr)  #array('i', [66, 56, 55, 45, 34])
print(arr1) #array('i', [66, 56, 11, 45, 34])

#another way of copying using typecode() and loop
arr2 = array(arr.typecode, (n for n in arr))
# use arr.typecode when we don't know the type the first array and using loop instead of convertin
#into list saves memory because we not creating extra list

#take input and assign to array
arr3 = array('i', [])
for _ in range(5):
    n = int(input('enter number in array'))
    arr3.append(n)
print(arr3)