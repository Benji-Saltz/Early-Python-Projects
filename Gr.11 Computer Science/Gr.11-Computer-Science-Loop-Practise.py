#Name: Benji Saltz
#Date: 9/29/16
#Description: All documents are in one folder

#Question 1- Backwards count
num=(int(input("input a number from 1-100:")))
if num<=100:
    for i in range(100,num-1,-1):
        print(i)
else:
    print("ERROR")
#Question 2-Times table
print("TIMES TABLE")
num1=(int(input("input a number from 2-12:")))
if num1<=12 and num1>=2:
    for j in range(1,13):
        print(num1,"times",j,"=",num1*j)
else:
    print("Error")
#Question 3-Guessing game
print("GUESSING GAME")
import random
numran=random.randint(1,10)
trial=5
while True:
    if trial==0:
      print("YOU SUCK GET OUT")
      break
    else:
        num2=(int(input("input a number from 1-10 to guess the right number:")))
        if num2>numran:
            print("TOO DAMN HIGH")
            trial-=1
        elif num2<numran:
            print("TOO DAMN LOW")
            trial-=1
        elif num2==numran:
            print("YOU GOT IT")
            break
      
#Question 4-Factorial
num3=(int(input("input a number from 1-20:")))
if num3<=20 and num3>=1:
    count1=1
    for k in range(1,num3+1):
        count1*=k
        print(num3,"times",k,"=",num3*k)
    print(num3,"!=",count1)
#Question 5-Average
count=1
print("Let me average out your marks!")
mark=(int(input("enter a mark:")))
print("Your average is:",mark/count)
markreply=(str(input("Would you like to put in another mark?"))).lower()
while(markreply=='yes'):
    count+=1
    mark=mark+(int(input("Put another mark:")))
    print("Your average is:",mark/count)
    markreply=(str(input("Would you like to put in another mark?"))).lower()
while(markreply=='no'):
    print("bye")
    break
#Question 6-Nested loops
width=int(input("enter a width:"))
for u in range(1,width+1):
    print('*'*u)
for u in range(width-1,0,-1):
    print('*'*u)
for u in range(0,width):
    print(' '*u,end='')
    for h in range(1,(width+1)-u):
        print(h,end='')
    print('')
        
    
    
    

