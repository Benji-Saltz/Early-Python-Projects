#Benji Saltz

#Question 1
number=str(input("Input a binary phrase:"))
count=0
count1=0
if(number[0]=='1'):
for i in range(0,len(number)):
    if(number[i]=='0'):
        count+=1
        if(i!=len(number)-1 and number[i+1]!='0'):
            print(count,end='')
            count=0
    else:
        count1+=1
        if(i!=len(number)-1 and number[i+1]!='1'):
            print(count1,end'')
            count1=0
if(count!='0'):
    print(count,end='')
else:
    print(count1,end='')
    

#Question 2


            
