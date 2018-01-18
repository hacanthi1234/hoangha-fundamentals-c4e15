from getpass import getpass
username = str(input("username: "))

password = str(getpass("password: "))

if username == "hacanthi1234" :

    if password == "hoangha1234"  :
        print("welcome user Ha dz")
    else:
        print("Password is not invalid.")

else:
    print("Invalid account")
