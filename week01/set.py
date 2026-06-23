# Set is a collection of unordered unique elements
set = {22, 23, 22, 25, 26}
print(set)      # {25, 26, 22, 23}  unordered unique i.e 22 came only once (saved on the basis of hash values)
print(22 in set)    #True
print(max(set))    #26

set1 = {2, 3, 4, 5, 6, 7}
set2 = {3, 5, 7}
print(set1 | set2)      #union
print(set1 - set2)      #difference
print(set1 & set2)      #intersaction