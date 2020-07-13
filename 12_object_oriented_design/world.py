"""
Section 12.3
World class

Discovering Computer Science, Second Edition
Jessen Havill
"""

import math

def _distance(point1, point2):
    """Return the distance between two positions."""
    
    diffX = point1[0] - point2[0]
    diffY = point1[1] - point2[1]
    return math.sqrt(diffX ** 2 + diffY ** 2)

class World:
    """A two-dimensional world class."""
    
    def __init__(self, width, height):
        """Construct a new flat world with the given dimensions."""
           
        self._width = width
        self._height = height
        self._agents = { }
        
    def getWidth(self):
        """Return the width of self."""
        
        return self._width
        
    def getHeight(self):
        """Return the height of self."""
        
        return self._height
    
    def __getitem__(self, position):
        """Return the agent at the given position."""
       
        if position in self._agents:
            return self._agents[position]
        return None
    
    def __setitem__(self, position, agent):
        """Set the given position to contain agent."""
       
        if (position not in self._agents) and \
           (position[0] >= 0) and (position[0] < self._width) and \
           (position[1] >= 0) and (position[1] < self._height):
            self._agents[position] = agent
            
    def __delitem__(self, position):
        """Delete the agent at the given position."""
        
        if position in self._agents:
            del self._agents[position]
        
    def neighbors(self, position, distance):
        """Return a list of agents within distance of
           position (a tuple)."""
        
        neighbors = []
        for otherPosition in self._agents:
            if (position != otherPosition) and \
               (_distance(position, otherPosition) <= distance):
                neighbors.append(self._agents[otherPosition])
        return neighbors

    def stepAll(self):
        """All agents advance one step in the simulation."""
        
        agents = list(self._agents.values())
        for agent in agents:
            agent.step()
