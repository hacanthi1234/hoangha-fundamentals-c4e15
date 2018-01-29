n = int(input("please insert a number: "))

x = 1
count = 0
while x < n:
    x +=1
    if n % x == 0:
        count += 1
if count > 2:
    print ("{0} is not a prime number".format(n))
else:
    print ("{0} is a prime number".format(n))
