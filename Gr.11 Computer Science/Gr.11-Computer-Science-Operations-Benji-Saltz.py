#By: Benji Saltz
#Description: All files are in one document
#Date: 9/13/16
print("Question 1")
a=int(input("enter an integer for a: "))
b=int(input("enter an integer for b: "))
print("\t",a,"+",b,"=",a+b)
print("\t",a,"-",b,"=",a-b)
print("\t",a,"x",b,"=",a*b)
print("\t",a,"/",b,"=",round(a/b,2))

print("Question 2")
import math
side1=(float(input("enter a size for side 1: ")))
side2=(float(input("enter a size for side 2: ")))
hypotenus=math.sqrt((side1**2)+(side2**2))
print("the hypotnuse is",round(hypotenus,2),"while side 1=",side1, "and side2=",side2)

print("Question 3")
number=float(input("enter a number: "))
print("Number\t\tSquare\t\tCube\t\t")
print(number,"\t\t",number**2,"\t\t",number**3,"\t\t")

print("Question 4")
x=float(input("enter an number to work in equation: "))
print("Number\t\tPolynomial")
print(x,"\t\t",round(((3*x)**4)-((10*x)**3)+(13),1))

print("Question 5")
course1=int(input("enter mark for first period: "))
course2=int(input("enter mark for second period: "))
course3=int(input("enter mark for third period: "))
course4=int(input("enter mark for fourth period: "))
print("If the marks are", course1,course2,course3,course4, "then the average is: ",round((course1+course2+course3+course4)/4,0))

print("Question 6")
names=str(input("Name: "))
hours=int(input("Hours worked in a week: "))
wage=int(input("wage per hour: "))
print("Name : ",names,"You work ", hours,"a week", "and make $",wage, "an hour")
print("You make $", round(hours*wage,2), "a week")




