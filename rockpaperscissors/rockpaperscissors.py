import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
userinput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer = random.randint(0,2)

if userinput >= 3:
    print("The inputted value is invalid")
else:
    if userinput == 0:
        print(rock)
    elif userinput == 1:
        print(paper)
    elif userinput == 2:
        print(scissors)

    print("Computer chose")

    if computer == 0:
        print(rock)
    elif computer == 1:
        print(paper)
    else:
        print(scissors)
    if computer == 1 and userinput ==0 :
        print("The computer won")
    elif computer == 2  and userinput == 1:
        print("The computer won")
    elif computer == 0 and userinput == 2:
        print("The computer won")
    elif computer == userinput:
        print("Its a draw")
    else:
        print("The user won")