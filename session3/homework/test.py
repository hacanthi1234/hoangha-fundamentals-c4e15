print("""
Hi there
think about a number from 0 -100, then press Enter
""")




lo = 0
hi = 100
loop = True
while loop:
    mid = (lo + hi) // 2
    answer = input("Is" + str(mid) + " your number?")
    if answer.lower() == "c":
        print("I knew it")
        loop = False
    elif answer.lower() == "s":
        hi = mid
    elif answer.lower() == "l":
        lo = mid
