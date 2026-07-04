from functools import reduce 

# filter()	Keep items that meet a condition	
# map()	Transform every item	
# reduce()	Combine all items into one result

nums = [2, 3, 4, 5]

cube = list(map(lambda n: n**3, nums))  #takes each element cubes it and stores in cube
print(cube)

sum = reduce(lambda x, y: x + y, cube)
print(sum)