num = input("Geuess the number between 1 and 10 ")
num = int(num)
while True:
    if num == 6:
        print("Correct...good job")
        break
    else:
        num = input("Wrong! Geuess the number again between 1 and 10 ")
        num = int(num)