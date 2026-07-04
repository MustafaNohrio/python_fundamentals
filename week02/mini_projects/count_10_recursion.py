num = 1
def count():
    global num

    print(num)
    num += 1
    
    if num == 11:
        return
    count()

count()