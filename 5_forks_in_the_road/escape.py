"""
Compute the number of steps required for a randomly moving
particle to escape a square room with width 100.

Discovering Computer Science, Second Edition
Jessen Havill
"""

import random
import turtle
    
def escape(width):
    """Compute the number of steps required for a randomly moving
       particle to escape a square room with a door.
    
    Parameter:
        width: the width of the room
        
    Return value: the number of steps needed to escape
    """
    
    step = 15       # standard deviation of one particle step
    radius = 10     # radius of the particle
    
    # draw the room and create a turtle named particle
    
    room = turtle.Turtle()
    room.hideturtle()
    room.up()
    room.pensize(5)
    room.pencolor('red')
    
    room.goto(-width, -width)
    room.down()
    for side in range(3):
        room.forward(2 * width)
        room.left(90)
    
    room.forward(width - 2 * radius)  # draw the door
    room.up()
    room.forward(4 * radius)
    room.down()
    room.forward(width - 2 * radius)
    
    particle = turtle.Turtle()       # the particle
    particle.speed(1)
    particle.shape('circle')
    particle.resizemode('user')
    particle.shapesize(radius / 20)
    particle.color('blue')
    particle.up()

    x = 0          # position of the particle
    y = 0
    escaped = False
    numSteps = 0
    while not escaped:
        numSteps = numSteps + 1
        dx = random.gauss(0, step)  # normal with mean 0 and std dev step
        dy = random.gauss(0, step)
        x = x + dx
        y = y + dy
        
        if ((x <= -width + radius) and ((y < -radius) or (y > radius))) \
          or (x >= width - radius) or (y <= -width + radius) \
          or (y >= width - radius):
            x = x - dx
            y = y - dy
        elif (x <= -width + radius) and ((y >= -radius) and (y <= radius)):
            escaped = True

        particle.goto(x, y)
        
    return numSteps

def main():
    escape(100)

main()
