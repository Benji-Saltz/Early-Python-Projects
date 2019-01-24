#Name: Benji Saltz
#Date: 17/11/16
#Description: Enter two words to see if they are anagrams (contain the same letters)
'''
(str,int)->none
Tests to see if words are anagrams

ex.1
Enter a word: hello
Enter another: hlleo
True
Yay you got yourself an anagram right there!

ex.2
Enter a word: helo
Enter another: hello
False
No anagrams here

'''
def are_anagrams(word1,word2):
    
    for i in range(0,len(word1)):
        characters1.append(ord(word1[i]))
        characters1.sort()
    for i in range(0,len(word2)):
        characters2.append(ord(word2[i]))
        characters2.sort()
    for i in range(0,len(word1)):
        if (characters1[i]!=characters2[i]):
            return (str(False) + "\nNo anagrams here")
    return (str(True) + "\nYay you got yourself an anagram right there!")
word1=input("Enter a word: ")
word2=input("Enter another: ")
characters1=[]
characters2=[]
print(are_anagrams(word1,word2))
    
           
