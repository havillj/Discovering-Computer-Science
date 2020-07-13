"""
Project 12.1

Discovering Computer Science, Second Edition
Jessen Havill
"""

from point import *
from time import *
from track import *
import math
import turtle

MAP_FILENAME = 'muni.gif' # background image file name
MAP_WIDTH = 770           # width of background image muni.gif
MAP_HEIGHT = 657          # height of background image muni.gif
MIN_LONG = -122.5256      # longitude range represented in muni.gif
MAX_LONG = -122.3564
MIN_LAT = 37.7        # latitude range represented in muni.gif
MAX_LAT = 37.82

tracks = { }              # global dictionary of tracks
                          # (must be global so it is accessible in clickMap)

def degToPix(geoPoint):
    """Convert a Point object containing a geographical location to a tuple
       representing the equivalent pixel in the graphics window."""
       
    long = geoPoint.getX()
    lat = geoPoint.getY()
    x = -(MAP_WIDTH / 2) + MAP_WIDTH * ((long - MIN_LONG) / (MAX_LONG - MIN_LONG))
    y = -(MAP_HEIGHT / 2) + MAP_HEIGHT * ((lat - MIN_LAT) / (MAX_LAT - MIN_LAT))
    return (x, y)
                
def pixToDeg(turtlePoint):
    """Convert a Point object containing a pixel location in the graphics window
       to a tuple representing the equivalent geographical location."""
       
    x = turtlePoint.getX()
    y = turtlePoint.getY()
    long = MIN_LONG + ((x + MAP_WIDTH / 2) / MAP_WIDTH) * (MAX_LONG - MIN_LONG)
    lat = MIN_LAT + ((y + MAP_HEIGHT / 2) / MAP_HEIGHT) * (MAX_LAT - MIN_LAT)
    return (long, lat)
        
def readTracks(fileName):
    """Read tracking info from a file into a dictionary of Track objects."""
    
    pass 

def clickMap(x, y):
    """Respond to a mouse click in the graphics window at position (x, y)
       by drawing the closest track and listing the times that the track
       comes within 100 meters of that position."""
    
    if (x < -MAP_WIDTH / 2) or (x > MAP_WIDTH / 2) or (y < -MAP_HEIGHT / 2) or (y > MAP_HEIGHT / 2):
        return
        
    tortoise = turtle.Turtle()
    screen = tortoise.getscreen()
    screen.clear()                 # clear the graphics window (and mouse click binding)
    screen.bgpic(MAP_FILENAME)     # redraw the background map
    tortoise.pencolor('red')
    tortoise.up()
    tortoise.goto(x, y)
    tortoise.down()
    tortoise.dot(10)               # plot the clicked-upon point
    tortoise.dot(10)
    tortoise.hideturtle()
    screen.update()
    
    long, lat = pixToDeg(Point(x, y))
    location = Point(long, lat)        # convert (x, y) to (long, lat)
    
    # find closest track and the times when it comes 
    #   within 100 meters of location
    
    trackNames = list(tracks.keys())
    minDist, minTimes = tracks[trackNames[0]].closestDistance(location, 0.1)
    for name in trackNames[1:]:
        distance, times = tracks[name].closestDistance(location, 0.1)  # 100 meters
        if distance < minDist:
            minDist = distance
            minName = name
            minTimes = times
    
    # write the times in the graphics window
    
    tortoise.up()
    tortoise.goto(MAP_WIDTH / 2 + 10, MAP_HEIGHT / 2)
    tortoise.pencolor('black')
    tortoise.write('Vehicle number ' + name, font = ('Helvetica', 12, 'bold'))
    tortoise.goto(MAP_WIDTH / 2 + 10, MAP_HEIGHT / 2 - 20)
    tortoise.write('Closest distance: {:4.2f} km'.format(minDist), font = ('Helvetica', 12, 'bold'))
    tortoise.goto(MAP_WIDTH / 2 + 10, MAP_HEIGHT / 2 - 40)
    tortoise.write('Times:', font = ('Helvetica', 12, 'bold'))
    skip = 55
    for index in range(len(times)):
        if index == 0 or times[index - 1].duration(times[index]) >= 300:  # 5 minutes
            tortoise.goto(MAP_WIDTH / 2 + 10, MAP_HEIGHT / 2 - skip)
            tortoise.write('  ' + str(times[index].time()), font = ('Helvetica', 10, 'normal'))
            skip = skip + 13

    tracks[minName].draw(degToPix)     # draw the track
    screen.onclick(clickMap)           # reassign this function to be called 
                                       #   on a mouse click

def main():
    global tracks
    tracks = readTracks('muni_tracking.csv')   # read tracks into a dictionary of tracks

    george = turtle.Turtle()           # set up turtle window with background map
    screen = george.getscreen()
    george.hideturtle()
    screen.setup(1200, 800)
    screen.bgpic(MAP_FILENAME)        # draw the map in the center of the window
    screen.onclick(clickMap)          # set event handler to call clickMap when a mouse click occurs
    screen.mainloop()                 # enter main event loop to wait for mouse clicks

main()
