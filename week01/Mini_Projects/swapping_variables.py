a = 4
b = 6
print(f"a: {a}")
print(f"b: {b}")

c = a
a = b
b = c
print(f"a: {a}")
print(f"b: {b}")

#without using extra variable
a = a + b
b = a - b
a = a - b
print(f"a: {a}")
print(f"b: {b}")

#python shortcut
a,b = b,a
print(f"a: {a}")
print(f"b: {b}")