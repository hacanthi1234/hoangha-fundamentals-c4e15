number = 0
x = int(input("enter a number"))

while x > 1:
    for i in range (1, x):
        if x % i == 0:


            print("prime number")
            break

        else:
            print("not prime number")
            break
