data = {0:22, 1:23, 2:24, 3:25}     #index:value > key-value pair
print(data[1])  #23

data = {'mustafa':22, 'hamza':23, 'imran':24, 'sajad':25}     #index(key) can be anything
print(data)     #{'mustafa': 22, 'hamza': 23, 'inran': 24, 'sajad': 25}
print(data['mustafa'])      #22
print(data.get('mustafa'))      #22 
print(data.get('mustafa', 'not found'))      #22 
print(data.get('ali', 'not found'))      #not found 

data2 = {'mustafa':22, 'hamza':22, 'imran':22, 'mustafa':25}     #with repeating key nd values
print(data2)     #{'mustafa': 25, 'hamza': 22, 'imran': 22}  >values are reapeated but keywords are not repeated because 
                 #key are collection of set and values are collection of list

# Creating a dictionary from set and list
keys = {'mustafa', 'hamza', 'imran', 'sajad'}  
values = [22, 23, 24, 25]
dictinary = dict(zip(keys, values))     #zip() combines set(krys) and list(values)
                                        #dict() converts it into a dictionary > pairing
print(dictinary)    #{'mustafa': 22, 'inran': 23, 'sajad': 24, 'hamza': 25}


# Operations
dictinary.pop('sajad')  #remove
print(dictinary)
dictinary['ali'] = 77   # adding an element(key-value)
print(dictinary)
del dictinary['imran']  #remove
print(dictinary)
