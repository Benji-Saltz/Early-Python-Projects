#1.PrintBox
########################################
# Programmer:Benji Saltz
# Date: oct.19/16
# File Name: printbox.py
# Description: makes a box by someone entering height and with with an added symbol to make the shape
########################################
def printBox(height,width,symbol):
    """
    (int,int,str)->none
    return the dimensions of the box with the embedded symbol
    >>>printBox(3,3,'&')
    &&&
    &&&
    &&&
    """
    box=''
    for i in range(height):
        for j in range(width):
            box+= symbol +' '
        box+='\n'
        print(box)


            
