########################################
# Programmer:Benji Saltz
# Date: oct.17/16
# File Name: numberToMonth.py
# Description: Template for a function
########################################

def numberToMonth(monthNumber):
    """ (int) -> (str)

    Return a 3-letter month abbreviation of a month number.
    
    >>> numberToMonth(1)
    'Jan'
    >>> numberToMonth(8)
    'Aug'
    """
#

    # write your code here
    month=("JanFebMarAprMayJunJulAugSepOctNovDec")
    
    return month[(monthNumber-1)*3:monthNumber*3]
#
########################################
if __name__ == '__main__':
    import doctest
    doctest.testmod()
