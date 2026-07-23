print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total = (bill * (12/100 + 1))
div = (total/people)
final = round(div,2)

print(f"Money to be paid by each person is: {final} ")