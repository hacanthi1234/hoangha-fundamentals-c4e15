from random import randint


x = randint(1,100)



loop = True
while(loop):
    number = int (input("Enter a number from 1 -100"))

    if number == x:
        print(" you are handsome")
        loop = False
    elif number < x:
        print("too small")
    else:
        print("too large")
