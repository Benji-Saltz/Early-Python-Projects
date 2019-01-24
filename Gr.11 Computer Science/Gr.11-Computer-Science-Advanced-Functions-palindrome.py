#5
########################################
# Programmer:Benji Saltz
# Date: oct.19/16
# File Name: palindrome.py
# Description: Shows if the word entered is a palindrome or not
########################################
def palindrome():
    """
    (str)->(str)
    checks if submitted word is a palindrome(true) or not(false)
    ex.
    Enter a word to check: racecar
    >>>True

    Enter a word to check: hello
    >>>False
    """
#main
    if(word==word[::-1]):
        return True
    else:
        return False
word = str(input("Enter a word to check: "))
print(palindrome())

