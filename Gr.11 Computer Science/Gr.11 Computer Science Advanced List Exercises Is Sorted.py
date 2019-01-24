#Name: Benji Saltz
#Date: 17/11/16
#Description: Tests that numbers entered are in order or not
'''
(str)-> none
Tests to see if numbers are in order

ex.1
Enter numbers:5 3 4
['5', '3', '4']
['3', '4', '5']
['3', '4', '5']
It's not in order

ex.2
Enter numbers:3 4 5
['3', '4', '5']
['3', '4', '5']
['3', '4', '5']
It's in order

'''
def Is_sorted(order):
    order2=order[:]
    order2.sort()
    print(order)
    print(order2)
    for i in range(0,len(order)):
        if(order2[i]!=order[i]):
            print(order2)
            return "It's not in order"
    print(order2)
    return "It's in order"
order=str(input("Enter numbers:"))
print(Is_sorted(order.split(" ")))



            
