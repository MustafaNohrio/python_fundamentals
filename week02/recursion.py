def greet():
    print('Hello')
    greet()
#greet()     #the function called itself in a loop for 1000 times(limit by default)

#check limit
import sys
print(sys.getrecursionlimit())  #1000 default limit
sys.setrecursionlimit(3000)
print(sys.getrecursionlimit())  #3000 limit

greet() # #the function called itself in a loop for 3000 times
# WARNING: this file demonstrates infinite recursion — do not run greet()