#3
########################################
# Programmer:Benji Saltz
# Date: oct.19/16
# File Name: encoder.py
# Description: Makes letters of a word translate to ascii and shows what symbols represent the word
########################################
def messageencoder():
    """
    (str)->(str)
    turns the letters of the word to symbols according to the ascii outcome

    enter a sentence: I am coding
    >>>hkd(`lh`mm
    """
    #main
    import random
    text=''

    for i in range(0,len(sentence)):
        addtract = random.randint(1,10)
        code=ord(sentence[i])

        if(addtract%2==0):
            code2=code+addtract
        else:
            code2=code-addtract
        text+=chr(code2)
    return text
sentence = str(input("enter the sentence: "))
print(messageencoder())
