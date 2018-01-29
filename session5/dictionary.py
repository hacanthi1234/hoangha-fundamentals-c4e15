dic = {

    "ng": "Người, nói về con người",
    "pt": "phát triển",
    "r": "rồi",
    "stt": "status",
    "ngta": "người ta"


}

while True:


    for key in dic:
        print(key, end = ' ')

    print()
    yourcode = input("Your code?")

    if yourcode in dic:
        print("translation: ",dic[yourcode])
    else:
        print("dunno")
        exp = input("Add your translation: ")
        dic[yourcode] = exp
        for key in dic:
            print(key, end = ' ')
