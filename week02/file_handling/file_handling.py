#reading from a file
file1 = open('week02/file_handling/data.txt', 'r')  #define directory if file not in root directry ie is in subfolder
print(file1)       #<_io.TextIOWrapper name='data.txt' mode='r' encoding='cp1252'>

print(file1.readline()) #reads only first line
print(file1.readline()) #reads seond line :as it has built in pointer which moved to second line

print(file1.read())  #all data in the file
file1.close()   #closing file to save resources

#>> good practice
with(open('week02/file_handling/data.txt', 'r') as file2):  #Automatically closes the file after with() block execution
     print(file2.read())

#Writing to the file
with(open('week02/file_handling/abc.txt', 'w') as file3): #'w' will create a file if not exist
    #  file3.write('Python \n')   #Python
    #  file3.write('Developer')   #Python
    #                             #Developer
     file3.write('GM ')   #GM >write() overwrites
     
with(open('week02/file_handling/abc.txt', 'a') as file3): #'a' will not overwrite it will add text ad the end
    file3.write('is  good person.') #GM is  good person.

#Copy all data from data.txt to abc.txt
with(open('week02/file_handling/data.txt', 'r') as file1):
     with(open('week02/file_handling/abc.txt', 'w') as file2):
          for data in file1:
               file2.write(data) 

#Creating a file
try:
     file = open('week02/file_handling/file.txt', 'x')
     #python raiss a FileExistsError if file already exists
except FileExistsError:
     print('file already exists')



#copy image to another file
with(open('week02/file_handling/my_picture.png', 'rb') as pic):  #rb is for read binary b/c image cannot be read as character
    #  print(pic.read())  #values of image
    pic2 = open('week02/file_handling/my_picture2.png', 'wb')    #wb for write binary
    #creating my_picture2.png and copying my_picture.png into it
    for i in pic:
         pic2.write(i)