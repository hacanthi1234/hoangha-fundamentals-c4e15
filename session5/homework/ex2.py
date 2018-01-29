numbers = [1, 6, 8, 1, 2, 1, 5, 6]

numb = input("Enter a number?")


count_numbers = {}
for x in numbers:
    if x in count_numbers:
        count_numbers[x] += 1
    else:
        count_numbers[x] = 1

for k, v in count_numbers.items():
    if numb == k:
        m = v
        print("{0} appears {1} times in my list".format(numb, m))
        break
else:
    print("0")
