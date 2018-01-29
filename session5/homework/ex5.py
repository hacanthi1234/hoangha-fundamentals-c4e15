print ("happy farm")
total = 1
add = []
for x in range(5):
    add.append(total)
    if x == 0:
        total = 1
    else:
        total = add[x] + add [x-1]

    print ("Month {0}: the farm has {1} pair(s)  of rabbit".format(x, total))
