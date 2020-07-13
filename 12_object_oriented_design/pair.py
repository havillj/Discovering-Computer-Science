"""
Section 12.3
Pair class (includes operators and special methods)

Discovering Computer Science, Second Edition
Jessen Havill
"""

class Pair:
    """An ordered pair class."""
    
    def __init__(self, a = 0, b = 0):
        """Constructor initializes a Pair object to (a, b).
        
        Parameter:
            self: a Pair object
            
        Return value: None
        """
        
        self._a = a   # the pair's first value
        self._b = b   # the pair's second value

    def getFirst(self):
        """Return the first value of self.
        
        Parameter:
            self: a Pair object
            
        Return value: the first value of self
        """
        
        return self._a
        
    def getSecond(self):
        """Return the second value of self.
        
        Parameter:
            self: a Pair object
            
        Return value: the second value of self
        """
        
        return self._b

    def get(self):
        """Return the (a, b) tuple representing self.
        
        Parameter:
            self: a Pair object
            
        Return value: the (a, b) tuple representing self
        """
        
        return (self._a, self._b)
        
    def __add__(self, pair2):
        """Return a new Pair representing the component-wise sum 
           of self and pair2.
           
        Parameters:
            self: a Pair object
            pair2: another Pair object
            
        Return value: a Pair object representing self + pair2
        """
       
        sumA = self._a + pair2._a
        sumB = self._b + pair2._b
        return Pair(sumA, sumB)
        
    def __sub__(self, pair2):
        """Return a new Pair representing the component-wise 
           difference between self and pair2.
           
        Parameters:
            self: a Pair object
            pair2: another Pair object
            
        Return value: a Pair object representing self - pair2
        """
       
        diffA = self._a - pair2._a
        diffB = self._b - pair2._b
        return Pair(diffA, diffB)
        
    def __mul__(self, scalar):
        """Return a new Pair representing self multiplied by scalar.
           
        Parameters:
            self: a Pair object
            scalar: a number
            
        Return value: a Pair object representing self * scalar
        """

        return Pair(self._a * scalar, self._b * scalar)
        
    def __truediv__(self, scalar):
        """Return a new Pair representing self divided by scalar.
           
        Parameters:
            self: a Pair object
            scalar: a number
            
        Return value: a Pair object representing self / scalar
        """

        return Pair(self._a / scalar, self._b / scalar)

    
    def set(self, a, b):
        """Set the two values in self.
        
        Parameters:
            self: a Pair object
            a: a number representing a new first value for self
            b: a number representing a new second value for self
            
        Return value: None
        """
        
        self[0] = a
        self[1] = b
        
    def scale(self, scalar):
        """Multiply the values in self by a scalar value.
        
        Parameters:
            self: a Pair object
            scalar: a number by which to scale the values in self
                        
        Return value: None
        """
        
        self.set(self._a * scalar, self._b * scalar)

    def __str__(self):
        """Return an '(a, b)' string representation of self.
        
        Parameter:
            self: a Pair object
            
        Return value: an '(a, b)' string representation of self
        """
        
        return '(' + str(self._a) + ', ' + str(self._b) + ')'
        
    def __eq__(self, pair2):
        """Return whether self and pair2 contain the same ordered pair.
           
        Parameters:
            self: a Pair object
            pair2: another Pair object
            
        Return value: 
            True if the corresponding values of self and pair2 are equal; 
            False otherwise
        """
        
        return (self._a == pair2._a) and (self._b == pair2._b)

    def __lt__(self, pair2):
        """Return whether self < pair2.
           
        Parameters:
            self: a Pair object
            pair2: another Pair object
            
        Return value: True if self < pair2; False otherwise
        """

        return (self._a < pair2._a) or \
               ((self._a == pair2._a) and (self._b < pair2._b))
  
    def __getitem__(self, index):
        """Return the first (index 0) or second (index 1) value
           in self.  For other index values, return None.
           
        Parameter:
            index: an integer (0 or 1)
            
        Return value: an element in a pair (or None)
        """
        
        if index == 0:
            return self._a
        if index == 1:
            return self._b
        return None
        
    def __setitem__(self, index, value):
        """Set the first (index 0) or second (index 1) value in
           self to the given value.
           
        Parameters:
            index: an integer (0 or 1)
            value: a number to which to set a value in self
            
        Return value: None
        """
        
        if index == 0:
            self._a = value
        elif index == 1:
            self._b = value
