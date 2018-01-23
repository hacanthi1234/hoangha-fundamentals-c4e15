print ("Hi there, here your favorite things so far ")

menu = ["death note", "netflix", "teaching"]

print(*menu, sep= ", ") #pythonic (only in python)

new_fav = str(input('name one thing you want to add?'))
menu.append(new_fav)
print(*menu, sep = ",") #sereparator ( chia dau phay)

# print(menu[-1])




#exercise:
# for i in range (len(menu)):
#     print (menu[i])  #for i

#for item in menu:
    #print(item)
