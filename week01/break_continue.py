#break keyword
for num in range(10):
    if num == 6:
        break    #stops the loop if num = 6
    print(num)

#continue keyword
for value in range(10):
    if value % 3 == 0:
        continue       #skips the iteration if value is divisible by 3
    print(value)