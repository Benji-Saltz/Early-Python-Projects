########################################
# Programmer:Benji Saltz
# Date: Nov.18/16
# File Name: Gr.11 Computer Science Tuple Excersize Bills and coins.py
# Description: Enter an amount of money and outputs how many of each bill is needed for exact change
########################################
import math
def Bills_and_coins(entered_money):
    '''
    (float)->(tuple)

    >>> Bills_and_coins(40.75)
    (2, 0, 0, 0, 0, 3)
    >>> Bills_and_coins(59.50)
    (2, 1, 1, 2, 0, 2)
    '''
    money=("$20 bill","$10 bill","$5 bill","$2 coin","$1 coin","25¢ coin")
    moneyVal=(20,10,5,2,1,0.25)
    a,b,c,d,e,f=money
    answer = ()
    for i in range(len(money)):
        remainder=(math.floor(entered_money/moneyVal[i]))
        entered_money-=(remainder*moneyVal[i])
        answer += (remainder,)
    return answer
###Main Function###Main Function###Main Function###Main Function###Main Function
entered_money=float(input("Enter an amount of money!: $"))
print(Bills_and_coins(entered_money))

if __name__=='__main__':
    import doctest
    doctest.testmod()
    
