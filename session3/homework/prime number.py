number = int(input("Enter a number:"))
if number == 2:
    print(number, "is a prime number")
elif number < 2:
    print(number, "is not a prime number")
else:
    i = 2
    while i < number:
        if number % i == 0:
            print(number, "is not a prime number")
            break
        i += 1
    else:
        print(number, "is a prime number")
