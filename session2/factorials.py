n = int(input("Product from 1 to n, along with n =? ")) + 1
factorial = 1

for i in range(1, n):
    factorial *= i

print(factorial)
