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
if userinput >= 0 and userinput <= 2:
    print(choiceimg[userinput])
computer = random.randint(0,2)
print("The computer chose:\n", choiceimg[computer])
if userinput >= 3 or userinput < 0:
    print("The entered choice is invalid!")
elif computer==1 and userinput==0:
    print("The computer won!")
elif computer==2 and userinput==1:
    print("The computer won!")
elif computer==0 and userinput==2:
    print("The computer won!")
elif computer==userinput:
    print("Its a draw!")
else:
    print("The user won!")