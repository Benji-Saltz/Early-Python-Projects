'''
BY: Benji Saltz
Date:25/10/16
Description: Function which creates a box from the number you submit
'''
def Boxfunction(height):

    """
    (int)=>(none)
    ex.
    Enter an integer: 3
    oooooo
    o    o
    oooooo
    Enter an integer: 10
    x x x x x x x x x x x x x x x x x x x x 
    x                                     x 
    x                                     x 
    x                                     x 
    x                                     x 
    x                                     x 
    x                                     x 
    x                                     x 
    x                                     x 
    x x x x x x x x x x x x x x x x x x x x        
    """
#main    
    box=''
    for i in range(int(height)):
        for j in range(int(height)*2):
            if((i!=0 or i!=int(height)-1) and (j==0 or j==(2*(int(height))-1))):
                if height>=1 and height<=9:
                    symbol='o'
                if int(height)<=21 and int(height)>=10:
                    symbol='x'
            elif(i==0 or i==height-1):
                if int(height)>=1 and int(height)<=9:
                    symbol='o'
                if int(height)<=21 and int(height)>=10:
                    symbol='x'
            else:
                symbol = " "
            box+= symbol +' '
        box+='\n'
    print(box)
    return (' ')

height = input("Enter an integer: ")

if (height.isdigit() and int(height)>=1 and int(height)<=21):
    print(Boxfunction(int(height)))
else:
    print("ERROR")
