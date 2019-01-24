########################################
# Programmer:Benji Saltz
# Date: oct.17/16
# File Name: minNumber.py
# Description: Template for a function
########################################

def minNumber(num1, num2, num3):
    """ (int, int, int) -> (int)

    Return the smallest of the three numbers.

    >>> minNumber(4, 7, 5)
    4
    >>> minNumber(100, 5, 5)
    5
    """

#

    # write your code here
    return min(num1,num2,num3)
#
########################################
if __name__ == '__main__':
    import doctest
    doctest.testmod()


