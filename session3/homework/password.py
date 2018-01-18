print("hi there, this is a superuser gateway")
n = 0


while n < 3:
    username = str(input("username: "))
    if username != "c4e":
        print ("you are not superuser")
    else:
        password = str(input("password: "))
        if password == "abc":
            print ("Welcome user")
        else:
            print ("password is incorrect")
        n += 1

else:
    print("you failed to log 3 times, go away noob.")
