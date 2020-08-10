import Constants
## DOCTEST
#####################
# allows writing tests based on expected output 
# from standard python interpreter along with documentation.
#####################
# also known as "document testing" or "testable document"
#####################
## Statements are written after primary prompt >>>
## Additional statements (like in multiline statements) are 
## written second line onwards after secondary prompt ...

## Expected output is written below the python statements 
# and it should be same as the result obtained, when you 
# run the statement 
#####################

#python3 ‑m doctest D:/Projects/Learn_ApplicationProgramming/TestFile1.txt
testFile1 = Constants.DATA_TST_FOLDER+'/TestFile1.txt'
print(testFile1)

def add2num(x, y):
    """Adds two given numbers and returns the sum.
    >>> add2num(6, 7)
    13
    >>> add2num(-8.5, 7)
    -1.5
    """
    return x + y

print(add2num(30, 100))

# Complete the following isPalindrome function:
def isPalindrome(x):
    # Write the doctests:
    """
    >>> isPalindrome(121)
    True
    >>> isPalindrome(344)
    False
    >>> isPalindrome(-121)
    Traceback (most recent call last):
    ValueError: x must be a positive integer
    >>> isPalindrome("hello")
    Traceback (most recent call last):
    TypeError: x must be an integer
    """
    # Write the functionality:
    if not (isinstance(x,int)):
        raise TypeError("x must be an integer")
    if(x<0):
        raise ValueError("x must be a positive integer")
    l_str=list(str(x))
    r_str=l_str[::-1]
    if l_str==r_str:
        return True
    else:
        return False


import math
# Define the class 'Circle' and its methods with proper doctests:
class Circle:
    def __init__(self, radius):
        # Define doctests for __init__ method:
        """
        >>> c1 = Circle(2.5); c1.radius
        2.5
        """
        self.radius = radius
        
    def area(self):
        # Define doctests for area method:
        """
        >>> c1 = Circle(2.5); c1.area()
        19.63
        """
        # Define area functionality:
        return round((math.pi*(self.radius**2)),2)
        
        
    def circumference(self):
        # Define doctests for circumference method:
        """
        >>> c1 = Circle(2.5); c1.circumference()
        15.71
        """
        # Define circumference functionality:
        return round((math.pi*self.radius*2),2)
    
