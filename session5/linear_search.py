numbers = [26, 9, 99, 6, 66, 90]

guess = int(input("Enter a number: "))

#assumption/ gia dinh ve ket qua
found_index = -1 #(means not found)

#create a loop to test our assumption
for index, number in enumerate(numbers):

    if number == guess:
        print("FOund at index:", index)
        break

else:
    print("Not found")



# loop = True
# while loop:
#
#     if guess in numbers:
#
#         x = numbers.index(guess)
#         print("Found {0} at index {1}".format(guess, x))
#         loop = False
#
#
# else:
#   print("Not found")
