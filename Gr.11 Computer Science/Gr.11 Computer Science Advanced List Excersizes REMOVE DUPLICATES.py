#Name: Benji Saltz
#Date: 17/11/16
#Description: Enter an input and any duplicates of letters will be taken out
'''
(str,int)->(str)
Removes duplicate letters

ex.1
Enter a list: heeellloo
['h', 'e', 'l', 'o']

ex.2
Enter a list: banana
['b', 'a', 'n']

'''
def remove_duplicates(word1):
    finalword=[]
    word2=[]
    for i in range(0,len(word1)):
        word2.append(ord(word1[i]))

    for i in range(0,len(word2)):
        if (chr(word2[i]) not in finalword):
            finalword.append(chr(word2[i]))
    return finalword

word1=input("Enter a list: ")
print(remove_duplicates(word1))
