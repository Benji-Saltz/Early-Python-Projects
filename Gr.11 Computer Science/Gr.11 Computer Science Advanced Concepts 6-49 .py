#Name: Benji Saltz
#Date: 17/11/16
#Description: Program randomly generates 6 numbers, 1-49
'''
(int)->(str)
Returns a month from a corresponding number which is inputed

ex.1
[7, 28, 6, 45, 3, 21]
ex.2
[26, 4, 42, 7, 30, 2]

'''
from random import randint
used_numbers=[]
numbers=[]
def SIX_FOURTY_NINE():
    for i in range(6):
        if (numbers not in used_numbers):
            numbers.append(randint(1,49))
        else:
            print("error")
    return (numbers)
    
print(SIX_FOURTY_NINE())
