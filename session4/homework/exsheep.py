sheepsize = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Ha and these are my sheep size")

biggest = max(sheepsize)
print ("Now my biggest sheep has size {0}, let's shear it".format(biggest))



print ("after shearing, here is my flock")
sheepsize[sheepsize.index(biggest)] = 8
print (sheepsize)

month = 1
loop = True
while loop:
    print('Month', month)
    print("One month has passed, here is my flock")
    for i, items in enumerate (sheepsize):
        sheepsize[i] = sheepsize[i] + 50

    print(sheepsize)

    biggest = max(sheepsize)
    print('Now my biggest sheep has size', biggest , "let's shear it")
    print('After shearing, here is my flock')
    sheepsize[sheepsize.index(biggest)] = 8
    print(sheepsize)
    month += 1

    if month == 4:
        loop = False

s = sum(sheepsize)
print("My flock has size in total: {0}".format(s))
money = s * 2
print('I would get', s, "*2","$ =", money, "$")
