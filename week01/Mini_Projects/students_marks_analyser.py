marks = []

for i in range(5):
    mark = float(input(f'Enter marks {i+1}: '))
    marks.append(mark)

print('maximum marks are', max(marks)) 
print('minimum marks are', min(marks))
print('average marks are', sum(marks)/len(marks)) 
print('range marks is', max(marks) - min(marks))