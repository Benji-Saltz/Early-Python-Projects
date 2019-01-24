########################################
# Programmer:Benji Saltz
# Date: oct.17/16
# File Name: stringToAscii.py
# Description: Template for a function
########################################

def stringToAscii(text):
    """ (str) -> (str)

    Return a string of ASCII codes of the characters in the text,
    separated by spaces.

    >>> stringToAscii("ABC")
    '65 66 67'
    >>> stringToAscii("Denison")
    '68 101 110 105 115 111 110'
    """

#

    # write your code here
    text2=''
    for letter in text:
        text2+=str(ord(letter))+' '
    return text2[:-1]
#
########################################
if __name__ == '__main__':
    import doctest
    doctest.testmod()


