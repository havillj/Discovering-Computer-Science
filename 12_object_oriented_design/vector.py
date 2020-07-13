"""
Section 12.3
Vector class

Discovering Computer Science, Second Edition
Jessen Havill
"""

import math

class Vector:
    """A two-dimensional vector class."""
    
    def __init__(self, vector = (0, 0)):
        """Constructor initializes a Vector object to <x, y>.
        
        Parameter:
            self: a Vector object
            
        Return value: None
        """
        
        self._x = vector[0]   # the vector's first coordinate
        self._y = vector[1]   # the vector's second coornidate

    def get(self):
        """Return the (x, y) tuple representing self.
        
        Parameter:
            self: a Vector object
            
        Return value: the (x, y) tuple representing self
        """
        
        return (self._x, self._y)
        
    def __add__(self, vector2):
        """Return the Vector that is self + vector2.
           
        Parameters:
            self: a Vector object
            vector2: another Vector object
            
        Return value: a Vector object representing self + vector2
        """
       
        sumX = self._x + vector2._x
        sumY = self._y + vector2._y
        return Vector((sumX, sumY))
        
    def __sub__(self, vector2):
        """Return the Vector that is self - vector2.
           
        Parameters:
            self: a Vector object
            vector2: another Vector object
            
        Return value: a Vector object representing self - vector2
        """
       
        diffX = self._x - vector2._x
        diffY = self._y - vector2._y
        return Vector((diffX, diffY))
    
    def set(self, x, y):
        """Set the two coordinates in self.
        
        Parameters:
            self: a Vector object
            x: a number representing a new first coordinate for self
            y: a number representing a new second coordinate for self
            
        Return value: None
        """
        
        self._x = x
        self._y = y
        
    def scale(self, scalar):
        """Multiply the coordinates in self by a scalar value.
        
        Parameters:
            self: a Vector object
            scalar: a number by which to scale the coordinates in self
                        
        Return value: None
        """
        
        self.set(self._x * scalar, self._y * scalar)

    def __str__(self):
        """Return an '<x, y>' string representation of self.
        
        Parameter:
            self: a Vector object
            
        Return value: an '<x, y>' string representation of self
        """
        
        return '<' + str(self._x) + ', ' + str(self._y) + '>'
        
    def __getitem__(self, index):
        """Return the value of the index-th coordinate of self.
           
        Parameter:
            index: an integer (0 or 1)
            
        Return value: a coordinate in a vector (or None)
        """
        
        if index == 0:
            return self._x
        if index == 1:
            return self._y
        return None
        
    def __setitem__(self, index, value):
        """Set the index-th coordinate of self to value.
           
        Parameters:
            index: an integer (0 or 1)
            value: a number to which to set a coordinate in self
            
        Return value: None
        """
        
        if index == 0:
            self._x = value
        elif index == 1:
            self._y = value

    def __mul__(self, scalar):
        """Return the Vector <x * scalar, y * scalar>.
           
        Parameters:
            self: a Vector object
            scalar: a numeric value
            
        Return value: a Vector that is self multiplied by scalar
        """

        return Vector((self._x * scalar, self._y * scalar))
        
    def __truediv__(self, scalar):
        """Return the Vector <x / scalar, y / scalar>.
           
        Parameters:
            self: a Vector object
            scalar: a numeric value
            
        Return value: a Vector that is self divided by scalar
        """

        return Vector((self._x / scalar, self._y / scalar))
 
    def magnitude(self):
        """Return the magnitude (length) of self.
        
        Parameter:
            self: a Vector object
            
        Return value: the magnitude of self
        """
        
        return math.sqrt(self._x ** 2 + self._y ** 2)
    
    def unit(self):
        """Return a unit vector in the same direction as self.
        
        Parameter:
            self: a Vector object
            
        Return value: a unit vector in the same direction as self
        """
        
        mag = self.magnitude()
        if mag > 0:
            return self / self.magnitude()
        return self
        
    def angle(self):
        """Return the angle made by self (in degrees).
        
        Parameter:
            self: a Vector object
            
        Return value: the angle made by self (in degrees)
        """
        
        return math.degrees(math.atan2(self._y, self._x))
        
    def turn(self, angle):
        """Rotate self by the given angle (in degrees).
        
        Parameters:
            self: a Vector object
            angle: the angle to rotate in degrees
            
        Return value: None
        """
        
        newAngle = math.radians(self.angle() + angle)
        self._x = math.cos(newAngle)
        self._y = math.sin(newAngle)
    
    def dotProduct(self, vector2):
        """Return the dot product of self and vector2,
           which is the cosine of the angle between them.
        
        Parameters:
            self: a Vector object
            vector2: another Vector object
            
        Return value: the dot product of self and vector2
        """
        
        return self._x * vector2._x + self._y * vector2._y
        
    def diffAngle(self, vector2):
        """Return the angle (in degrees) between self and vector2.
        
        Parameters:
            self: a Vector object
            vector2: another Vector object
            
        Return value: the angle (in degrees) between self and vector2
        """
        
        unit1 = self.unit()
        unit2 = vector2.unit()
        dot = unit1.dotProduct(unit2)
        if dot > 0.9999:
            return 0
        if dot < -0.9999:
            return 180
        return math.degrees(math.acos(dot))
        