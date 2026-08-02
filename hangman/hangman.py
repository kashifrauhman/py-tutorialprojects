import random
word_list = ["aardvark", "baboon", "camel"]

word = random.choice(word_list)

guess = input("Guess a letter from the word: ").lower()

for i in word:
    if i == guess:
        print("Right")
    else:
        print("Wrong")