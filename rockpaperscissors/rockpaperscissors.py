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
choiceimg = [rock, paper, scissors]
userinput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if userinput >= 0 and userinput <= 3:
    print(choiceimg[userinput])
if userinput > 3 and userinput < 0:
    print("The entered choice is invalid!")
computer = random.randint(0,2)
if computer > userinput:
    print("The computer won")