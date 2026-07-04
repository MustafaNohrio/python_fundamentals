nums = [10, 55, 32, 75, 90, 68]
#filter() is a built in function that takes a function(for logic) and an iterable
great = list(filter(lambda n: n > 50, nums))   #gives numbers one by one from list (nums) to lambda function and convert it to a list (great) > numbers greater than 50
print(great)