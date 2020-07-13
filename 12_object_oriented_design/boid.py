"""
Section 12.3
Boid class

Discovering Computer Science, Second Edition
Jessen Havill
"""

import random, turtle, math
from pair import *
from vector import *

TURN_ANGLE = 30

PREV_WEIGHT = 0.5
AVOID_WEIGHT = 0.25
MATCH_WEIGHT = 0.15
CENTER_WEIGHT = 0.1

AVOID_DISTANCE = 3
AVOID_ANGLE = 300
MATCH_DISTANCE = 10
MATCH_ANGLE = 240
CENTER_DISTANCE = 15
CENTER_ANGLE = 180

class Boid:
    """A boid in a agent-based flocking simulation."""
    
    def __init__(self, myWorld):
        """Construct a boid at a random position in the given world."""

        self._world = myWorld
        (x, y) = (random.randrange(self._world.getWidth()), 
                  random.randrange(self._world.getHeight()))
        while self._world[x, y] != None:
            (x, y) = (random.randrange(self._world.getWidth()), 
                      random.randrange(self._world.getHeight()))
        self._position = Pair(x, y)
        self._world[x, y] = self
        self._velocity = Vector((random.uniform(-1, 1), 
                                 random.uniform(-1, 1))).unit()
        self._turtle = turtle.Turtle()
        self._turtle.speed(0)
        self._turtle.up()
        self._turtle.setheading(self._velocity.angle())
        
    def move(self):
        """Move self to a new position in its world."""
    
        self._turtle.setheading(self._velocity.angle())
        
        width = self._world.getWidth()
        height = self._world.getHeight()
        
        newX = self._position[0] + self._velocity[0]
        newX = min(max(0, newX), width - 1)
        newY = self._position[1] + self._velocity[1]
        newY = min(max(0, newY), height - 1)
        
        if self._world[newX, newY] == None:
            self._world[newX, newY] = self
            del self._world[self._position.get()]
            self._position = Pair(newX, newY)
            self._turtle.goto(newX, newY)
            
        if (self._velocity[0] < 0 and newX < 5) or \
           (self._velocity[0] > 0 and newX > width - 5) or \
           (self._velocity[1] < 0 and newY < 5) or \
           (self._velocity[1] > 0 and newY > height - 5):
            self._velocity.turn(TURN_ANGLE)
            
    def neighbors(self, distance, angle):
        """Return a list of boids within distance and viewing angle."""
        
        neighbors = self._world.neighbors(self._position.get(), distance)
        visibleNeighbors = []
        for boid in neighbors:
            neighborDir = Vector((boid._position - self._position).get())
            if self._velocity.diffAngle(neighborDir) < angle:
                visibleNeighbors.append(boid)
        return visibleNeighbors
#        return [boid for boid in self._world.neighbors(self._position.get(), distance) if self._velocity.diffAngle(Vector((boid._position - self._position).get())) < angle]

    def _avoid(self):
        """Return a velocity away from close neighbors."""
        
        neighbors = self.neighbors(AVOID_DISTANCE, AVOID_ANGLE)
        if len(neighbors) == 0:
            return Vector()
        sumPosition = Pair()
        for boid in neighbors:
            sumPosition = sumPosition + boid._position
        avgPosition = sumPosition / len(neighbors)
        avoidVelocity = Vector((self._position - avgPosition).get())
        return avoidVelocity.unit()

    def _match(self):
        """Return the average velocity of neighboring boids."""
        
        neighbors = self.neighbors(MATCH_DISTANCE, MATCH_ANGLE)
        if len(neighbors) == 0:
            return Vector()
        sumVelocity = Vector()
        for boid in neighbors:
            sumVelocity = sumVelocity + boid._velocity
        return (sumVelocity / len(neighbors)).unit()
        
    def _center(self):
        """Return a velocity toward center of neighboring flock."""
        
        neighbors = self.neighbors(CENTER_DISTANCE, CENTER_ANGLE)
        if len(neighbors) == 0:
            return Vector()
        sumPosition = Pair()
        for boid in neighbors:
            sumPosition = sumPosition + boid._position
        avgPosition = sumPosition / len(neighbors)
        centerVelocity = Vector((avgPosition - self._position).get())
        return centerVelocity.unit()
            
    def step(self):
        """Advance self one step in the flocking simulation."""
    
        newVelocity = (self._velocity * PREV_WEIGHT + 
                       self._avoid() * AVOID_WEIGHT +    # rule 1
                       self._match() * MATCH_WEIGHT +    # rule 2
                       self._center() * CENTER_WEIGHT)   # rule 3
        
        self._velocity = newVelocity.unit()
        self.move()
