"""
Project 9.3

Discovering Computer Science, Second Edition
Jessen Havill
"""

import turtle
import random
import matplotlib.pyplot as pyplot

BLOCKED = 0  # site is blocked 
OPEN = 1     # site is open and empty
FULL = 2     # site is open and full

SCALE = 16   # drawing scale

def drawSquare(pos, color, tortoise):
    """Draws one square in the given color at the
       given position in the grid.
       
    Parameters: 
        pos: a (row, column) tuple
        color: a color string
        tortoise: a Turtle object
        
    Return value: None
    """
    
    (row, column) = pos
    screen = tortoise.getscreen()
    rows = int(screen.canvheight / screen.yscale)
    row = rows - row - 1
    tortoise.shape(color)
    tortoise.up()
    tortoise.goto(column, row + 1)
    tortoise.stamp()
    
def drawGrid(grid, tortoise):
    """Draws an empty grid using turtle graphics.
       
    Parameters: 
        grid: a 2D grid of open/blocked cells
        tortoise: a Turtle object
        
    Return value: None
    """
    
    rows = len(grid)
    columns = len(grid[0])
    for row in range(rows):
        for col in range(columns):
            if grid[row][col] == BLOCKED:
                drawSquare((row, col), 'black', tortoise)
            else:
                drawSquare((row, col), 'white', tortoise)
        
def createSquares(screen, colors):
    """Creates square shapes in the given colors to be used
       as turtle graphics stamps in a cellular automata.
       
    Parameters: 
        screen: a Screen object
        colors: a list of color strings
        
    Return value: None
    """
    
    square = ((0, 0), (0, SCALE), (SCALE, SCALE), (SCALE, 0))
    for color in colors:
        squareShape = turtle.Shape('compound')
        squareShape.addcomponent(square, color, 'gray')
        screen.register_shape(color, squareShape)

def randomGrid(rows, columns, p):
    """Create and return a random grid with vacancy 
       probability p."""

   pass

def dfs(grid, row, col, tortoise, draw):
    """Do a depth first search on grid starting at site 
       (row, col).  If draw == True, visualize the 
       percolation using tortoise."""
       
    pass

def percolates(grid, draw):
    """Decide whether a grid percolates.
       If draw == True, visualize the percolation with 
       turtle graphics."""
       
    rows = len(grid)
    columns = len(grid[0])
    if draw:
        tortoise = turtle.Turtle()
        screen = tortoise.getscreen()
        screen.setup(columns * SCALE + 20, rows * SCALE + 20)
        screen.setworldcoordinates(0, 0, columns, rows)
        screen.tracer(5)
        tortoise.hideturtle()
        createSquares(screen, ['black', 'white', 'blue'])
        drawGrid(grid, tortoise)
    else:
        tortoise = None
    
    # "POUR THE FLUID" HERE
        
    if draw:
        screen.update()
        screen.exitonclick()
        
    # RETURN TRUE OR FALSE
    
def percMonteCarlo(rows, columns, p, trials):
    """Use a Monte Carlo simulation to estimate the 
       percolation probability on a grid with vacancy 
       probability p."""

    pass
    
def percPlot(rows, columns, minP, maxP, stepP, trials):
    """Plot percolation probability vs. vacancy probability
       for vacancy probabilities between minP and maxP in 
       steps of stepP, using the given number of trials
       in the Monte Carlo simulation."""

    pass

def main():
    pass
    
main()
