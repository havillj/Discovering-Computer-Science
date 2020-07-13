"""
Section 12.3
Flocking simulation

Discovering Computer Science, Second Edition
Jessen Havill
"""

import turtle
from world import *
from boid import *

WIDTH = 100
HEIGHT = 100
NUM_BIRDS = 30
ITERATIONS = 2000

def main():
    worldScreen = turtle.Screen()
    worldScreen.setworldcoordinates(0, 0, WIDTH - 1, HEIGHT - 1)
    worldScreen.tracer(NUM_BIRDS)
    
    sky = World(WIDTH, HEIGHT)
    for index in range(NUM_BIRDS):
        bird = Boid(sky)
        
    for step in range(ITERATIONS):
        sky.stepAll()
            
    worldScreen.update()
    worldScreen.exitonclick()
    
main()
