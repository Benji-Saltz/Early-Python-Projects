#Name: Benji Saltz
#Discription: Everything is in one document
#1. Marks= Output of what letter grade you got
#2.Discount= Ticket sales with a discounted value if people buy tickets in groups
#3.Quadratic Roots= Calculates if real roots come out of quadratic formula
#4.Rates= Caluclates price of water between government, public and companies
#Date:9/20/16
#Question 1
mark=(float(input("Put in your mark")))
if mark>=80 and mark<=100 :
    print("Execelent work, it\'s an A!!!")
elif mark<=79 and mark>=70:
        print("Not bad, you got a B!")
elif mark<=69 and mark>=60:
            print("you barely passed! you got a C")
elif mark<=59 and mark>=50:
    print("you are ruining your life, you got a D")
elif mark<50 and mark>=0:
    print("Dig a grave you failed!")
elif mark>100 or mark<0:
    print("INVALID! INVALID! INVALID!")
                
#Question 2
print("Hey, welcome to the fair!")
print("tickets are $10.95 a person while group bigger than 5 cost $8.95 a person!")
ticket=(int(input("How many tickets would you like to purchase?")))
if ticket<5 :
            print("You purchased",ticket,"Tickets! That will be",round(10.95*ticket,2))
elif ticket>=5 and ticket<=50 : 
            print("You Purchased",ticket,"Tickets! That will be",round(8.95*ticket,2))
elif ticket>50:
    print("ERROR ERROR, YOU CANNOT PURCHASE IN THAT AMOUNT!")

#Question 3
import math
print("Lets do quadratics! ax**2+bx+x=0")
print(" We will be using -b+-sqrt(b**2-4ac)/2a")
a=float(input("What will represent a?:"))
b=float(input("What will represent b?:"))
c=float(input("What will represent c?:"))
d=(b**2)-4*a*c
if d>0:
        x1=-b+math.sqrt(d)/2*a
        x2=-b-math.sqrt(d)/2*a
        print(round(x1,2), "or", round(x2,2))
elif d==0:
        x3=-b/2*a
        print(round(x,2))
elif d<0:
        print("No real roots")
#Question 4
print("Welcome to the city water company!")
typ=(str(input("please enter what type you fall under: G for government, C for Company or P for public:")))
liter=(float(input("How much water did you use?:")))
if typ=='c' and liter<=1000:
    print("You are a company and used:",liter,"The subtotal is $",300,"With a total of $",(300*0.13)+300)
elif typ=='c' and liter>1000:
    print("You are a company and used:",liter,"The subtotal is $",round(300+(0.75*(liter-1000)),2),"With a total of $",round(((300+(0.75*(liter-1000)))*0.13)+(300+(0.75*(liter-1000))),2))
elif typ=='p' and liter<=100:
    print("You used:",liter,"The subtotal is $",round(0.77*liter,2),"With a total of $",round(((0.77*liter)*0.13)+(0.77*liter),2))

elif typ=='p' and liter>100:
    print("You used:",liter,"The subtotal is $",round(0.50*liter,2),"With a total of $",round(((0.50*liter)*0.13)+(0.50*liter),2))

elif typ=='g' and liter<=500:
    print("You are the government and used:",liter,"The subtotal is $:",200,"With a total of $",round((200*0.13)+200),2)

elif typ=='g' and liter<500:
    print("You are the government and used:",liter,"The subtotal is $:",400,"With a total of $",round((400*0.13)+400),2)
else:
    print("ERRROR ERROR ERROR")

    

