'''
By: Benji Saltz
Date:11/9/2016
Description: Three programs, one which finds highest mark and average,
another than sees how many a's are in a sentence
and one which find 3 younest and oldest out of 50 people
'''
import random
marks=[] #stores inputed marks
for i in range(5): #only allows 5
    marks.append(int(input("enter a mark: ")))#allows you to enter mark
print("Your hightest mark is: ",max(marks))#prints highest mark entered
print("Your average mark is: ",round(sum(marks)/len(marks)))#prints lowest mark entered
def count(letter):#stores how many a's have been entered
    return list(letter).count("a")#counts how many a's have been entered
print("you have",count(input("Enter a sentence: ").lower()),"a('s) in your sentence")
age=[]#allows 50 ages to be stored
for i in range(50):
    age.append(random.randint(1,100))#will randomize 50 ages from 1 to 100
age.sort()# allows ages to be sorted from lowest to highest
print("The three youngest out of 50 are ages: ",age[0],",",age[1],",&",age[2],"and the oldest out of 50 are ages: ",age[47],",",age[48],",&",age[49])#takes stored numbers from list which were sorted from lowest to highest and displays the 3 lowest and highest
