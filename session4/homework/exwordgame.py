import random

Words = ('champion', 'meticulous', 'car', 'physics','anaconda','mouse')
word = random.choice(Words)
correct = word
jumble = ''
guess = ''

jumble = ''.join(random.sample(word, k=len(word)))

print()
while True:
    print(jumble)
    guess = input('Your answer: ')
    if guess == word:
        print("Hura!")
        break
    else:
        print(":(")
