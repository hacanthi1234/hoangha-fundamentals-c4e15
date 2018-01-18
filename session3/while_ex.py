count = 0
while count < 5:

    yob = int(input("Your year of birth?"))
    age = 2018 - yob

    if age < 10:
        print("baby")
    elif age <18:
        print("teeager")
    else:
        print("adult")

    count += 1
    if count >= 5:
        break
