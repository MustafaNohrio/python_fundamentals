def outer():
    print('outer function')

    def inner():
        print('Inner function')

    return inner    #returning the function

outer()  #outer function
something = outer()
#we assigned the outer() funtion to something and the outer() returns a function something becomes a funtion
something() #outer function
            #Inner function
