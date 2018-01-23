print ("Hi there, here your favorite things so far")

menu = ["deathnote", "netflix", "teaching"]

print(*menu, sep = ',')

print("*" *30)


# position = 1
# for item in menu:
#     print ("{0}. {1}".format(position, item))
#     position += 1

for index, item in enumerate(menu):
    y = "{0}. {1}".format(index + 1, item)
    print(y)

print("*" *30)

# for index, item in enumerate(menu): #clones
#     menu[index] = item.lower()      #update original

# print(menu)
#
# menu.pop(0)
# print (menu)

x = int(input('Tell meh the position you want to get rid of'))

menu.pop( x - 1)

for index, item in enumerate(menu):
    y = "{0}. {1}".format(index + 1, item)
    print(y)
