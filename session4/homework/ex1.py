menu = ['T-Shirt', 'Sweater']


while True:
    x = str(input("Welcome to our shop, what do you want (C, R, U, D)?")).upper()


    if x == "R":
        print( "Our items: ", end = " ")
        print(*menu, sep = ",")

    elif x == "C":
        newitem = str(input("Enter new item: "))

        menu == menu.append(newitem)
        print( "Our items: ", end = " ")
        print(*menu, sep = ",")



    elif x == "U":
        newposition = int(input("Update position?"))
        menu[newposition - 1] = str(input("Enter new item: "))
        print( "Our items: ", end = " ")
        print(*menu, sep = ",")

    else:
        delete = int(input("Delete position?"))
        menu.pop( delete - 1 )
        print( "Our items: ", end = " ")
        print(*menu, sep = ",")

    
