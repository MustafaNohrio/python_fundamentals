#if
num = 6
if num % 2 == 0:
    print("Even")

if num % 2 != 0:
    print("Odd")

print("Bye!")


#if else
age = input("Enter your age ")
age = int(age)

if age >= 18:
    print("You are Eligible to vote.")

else:
    print("You are not Eligible to vote.")


#nested if
num = 4
salary = 8

if num%2 == 0:
    print("Even")
    if num < salary:
        print("Great!")
else:
    print("Odd")

print("Bye")

#elif (else if)
x = 5
if x == 1:
    print("one")
elif x == 2:
    print("two")
elif x == 3:
    print("three")
elif x == 4:
    print("four")
elif x == 5:
    print("five")
elif x == 6:
    print("six")
else:
    print("incorrect")