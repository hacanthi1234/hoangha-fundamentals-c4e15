from random import randint


x = randint(0, 100)

print("Random number(0-100)", x)

if x < 30:
    sad = input("(ಠ_ಠ)┌∩┐")
    print("sad")

elif 30<= x < 60:
    normal = input("(• ε •)")
    print("normal")

else:
    happy = input("✌(◕‿-)✌")
    print("happy")
