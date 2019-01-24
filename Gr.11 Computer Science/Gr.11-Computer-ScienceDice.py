#2.
########################################
# Programmer:Benji Saltz
# Date: oct.19/16
# File Name: dice.py
# Description: allows user to enter a number for how many times a dice could be rolled and displays what the dice rolled to each round
########################################
def Dice():
    """
    (int)->(none)
    return the outcomes of the dice rolls
    """
    #main
    import random
    return random.randint(1,6)
rollNumber= int(input("enter the number of times you want to roll the dice!: "))
if rollNumber<=5:
    for i in range(0,rollNumber):
        print(Dice())
else:
    print("error, lol ur bad")
    
            
        
