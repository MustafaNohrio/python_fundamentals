numbers = [10, 20, 30, 40, 50]

# Mean
mean = sum(numbers) / len(numbers)      #average
print('mean: ', mean)

# Median
numbers.sort()
#When number of values is odd 
median = numbers[len(numbers) // 2]    #value at middle index
print('median: ', median)

#When number of values is odd 
numbers.append(60)
numbers.sort()
median = (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2      #average of two values in middle
print('median(even): ', median)


# Mode
numbers = [1, 2, 2, 3, 4, 2, 5]
frequency = {}      #empty dictionary o store value:count
for num in numbers:
    if num in frequency:
        frequency[num] += 1 #if value is already resent in dictionary
    else:
        frequency[num] = 1
mode = max(frequency, key=frequency.get)    #key whose count is max
print('mode: ', mode)


# Central tendencies using 'statistics' module
import statistics

marks = [75, 80, 97, 75, 65, 75]

print('mean: ', statistics.mean(marks))
print('median: ', statistics.median(marks))
print('mode: ', statistics.mode(marks))