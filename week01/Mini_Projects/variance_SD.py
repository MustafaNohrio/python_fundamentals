data = [2, 4, 6, 8]

mean = sum(data) / len(data)

variane = 0

for i in data:
    sum = (i - mean) **2   #sum of squared distance of each data point from mean

variane = sum / len(data)   #average of squared sum

sd = variane **0.5  #square root of variance

print('mean', mean)
print('varince', variane)
print('stndard deviation', sd)