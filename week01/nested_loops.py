#suppose I want to print "hello G.M G.M G.M G.M" 5 times
i = 1
while i <= 5:
    print("hello", end="") #end="" means NO NEXT LINE
    j = 1
    while j <= 4:
        print(" G.M", end="")
        j += 1 
    i += 1
    print()

print(i)