"""
Project 12.1
Track class

Discovering Computer Science, Second Edition
Jessen Havill
"""

from point import *
from time import *
import turtle
import math

class Track:
    """A sequence of geographical points with time stamps that track
       a moving object."""
       
    def __init__(self, name):
        pass
        
    def _distance(self, point1, point2):
        """Return the approximate distance (in km) between two geographical points."""
        
        kmPerLat = 111.0
        kmPerLong = 111.32 * math.cos(math.radians(abs(point1.getY() + point2.getY()) / 2))
        differenceLong = abs(point1.getX() - point2.getX())
        differenceLat = abs(point1.getY() - point2.getY())
        kmLong = differenceLong * kmPerLong
        kmLat = differenceLat * kmPerLat
        distanceKm = math.sqrt(kmLong ** 2 + kmLat ** 2)
        return distanceKm
        
    def _distanceIndices(self, index1, index2):
        """Return the approximate distance (in km) between the two points
           in the track with the given indices."""
        
        point1 = self._points[index1]
        point2 = self._points[index2]
        return _distance(point1, point2)
        
    def _speed(self, index1, index2):
        """Return the approximate speed traveled between the two points
           in the track with the given indices."""
        
        pass
        
    def append(self, long, lat, date, time):
        """Add a point and time to the end of the track."""
        
        pass
        
    def __len__(self):
        """Return the number of points on the track."""
        
        pass
                
    def averageSpeed(self):
        """Return the average speed over the track."""
        
        pass
            
    def totalDistance(self):
        """Return the total distance traversed on the track."""
        
        pass
    
    def diameter(self):
        """Return the distance between the two points that are 
           farthest apart on the track."""
        
        pass
            
    def closestDistance(self, location, error):
        """Find the closest distance a point on the track comes to the 
           given point; return this distance and the time(s) when the 
           track comes within error of this distance."""
        
        pass
        
    def draw(self, degToPix):
        """Draw the track, using the degToPix function to convert each
           geographical point to an equivalent pixel location in the
           graphics window."""
        
        tortoise = turtle.Turtle()
        screen = tortoise.getscreen()
        tortoise.speed(0)
        tortoise.hideturtle()
        screen.tracer(10)
        tortoise.pencolor('blue')
        tortoise.up()
        tortoise.goto(degToPix(self._points[0]))
        tortoise.down()
        for p in self._points:
            tortoise.goto(degToPix(p))
