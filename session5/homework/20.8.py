string = "ThiS is String with Upper and lower case Letters"
alphabet = "abcdefghijklmnopqrstuvwxyz"
stringtext = string.lower()
numbers_of_letters = {}

for letter in stringtext:
    numbers_of_letters[letter] = numbers_of_letters.get(letter, 0) + 1

for i in alphabet:
    if i in numbers_of_letters:
        print (i, numbers_of_letters[i])
