import random
word_list = ["aardvark", "baboon", "camel"]

word = random.choice(word_list)

guess = input("Guess a letter from the word: ").lower()

wordLength = len(word)
print(wordLength)

placeholder = ""

for dash in range(0, wordLength):
    placeholder = placeholder + "_"

print(placeholder)

display = ""


for i in word:
    if i == guess:
        display += guess
    else:
        display += "_"

print(display)
