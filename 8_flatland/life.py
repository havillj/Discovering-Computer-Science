"""
Game of Life

Discovering Computer Science, Second Edition
Jessen Havill
"""

import turtle
import copy

ALIVE = 1      # value of a live cell
DEAD = 0       # value of a dead cell
SCALE = 16     # scale at which to draw the grid

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
    
def drawGrid(rows, columns, tortoise):
    """Draws an empty grid using turtle graphics.
       
    Parameters: 
        rows: the number of rows in the grid
        columns: the number of columns in the grid
        tortoise: a Turtle object
        
    Return value: None
    """
    
    tortoise.pencolor('gray')
    for row in range(rows + 1):
        tortoise.up()
        tortoise.goto(0, row)
        tortoise.down()
        tortoise.goto(columns, row)
    for column in range(columns + 1):
        tortoise.up()
        tortoise.goto(column, 0)
        tortoise.down()
        tortoise.goto(column, rows)
        
def createSquares(screen, colors):
    """Creates square shapes in the given colors to be used
       as turtle graphics stamps in a cellular automaton.
       
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
        
def emptyGrid(rows, columns):
    """Create a rows x columns grid of zeros.

    Parameters:
        rows: the number of rows in the grid
        columns: the number of columns in the grid

    Return value: a list of ROWS lists of COLUMNS zeros
    """
    
    grid = []
    for r in range(rows):
        row = [DEAD] * columns
        grid.append(row)
    return grid
    
def initialize(grid, coordinates, tortoise):
    """Set a given list of coordinates to 1 in the grid
       and draw them as black squares.

    Parameters:
        grid: a grid of values for a cellular automaton
        coordinates: a list of coordinates
        tortoise: a Turtle object

    Return value: None
    """

    for (r, c) in coordinates:
        grid[r][c] = ALIVE
        drawSquare((r, c), 'black', tortoise)
    
def neighborhood(grid, row, column):
    """Finds the number of live neighbors of the cell in the
       given row and column.
    
    Parameters:
        grid: a two-dimensional grid of cells
        row: the row index of a cell
        column: the column index of a cell
        
    Return value:
        the number of live neighbors of the cell at (row, column)
    """
    
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    rows = len(grid)
    columns = len(grid[0])
    count = 0
    for offset in offsets:
        r = row + offset[0]
        c = column + offset[1]
        if (r >= 0 and r < rows) and (c >= 0 and c < columns):
            if grid[r][c] == ALIVE:
                count = count + 1
    return count
    
def life(rows, columns, generations, initialCells, tortoise):
    """Simulates the game of life for the given number of
       generations, starting with the given live cells.
    
    Parameters:
        rows: the number of rows in the grid
        columns: the number of columns in the grid
        generations: the number of generations to simulate
        initialCells: a list of (row, column) tuples indicating
                      the positions of the initially alive cells
        tortoise: a Turtle object
        
    Return value:
        the final configuration of cells in a grid
    """
    screen = tortoise.getscreen()        # to display window title
    grid = emptyGrid(rows, columns)
    drawGrid(rows, columns, tortoise)
    initialize(grid, initialCells, tortoise)
    
    for g in range(generations):
        newGrid = copy.deepcopy(grid)
        for r in range(rows):
            for c in range(columns):
                neighbors = neighborhood(grid, r, c)
                if grid[r][c] == ALIVE and (neighbors < 2 or neighbors > 3):  # rules 1 and 3
                    newGrid[r][c] = DEAD
                    drawSquare((r, c), 'white', tortoise)
                elif grid[r][c] == DEAD and neighbors == 3:  # rule 4
                    newGrid[r][c] = ALIVE
                    drawSquare((r, c), 'black', tortoise)
        grid = newGrid
        screen.title('Generation ' + str(g))    # change window title
        
    return grid
    
def main():
    columns = 20   # number of columns in the grid
    rows = 20      # number of rows in the grid

    george = turtle.Turtle()
    screen = george.getscreen()
    screen.setup(columns * SCALE + 20, rows * SCALE + 20)
    screen.setworldcoordinates(0, 0, columns, rows)
    screen.tracer(5)
    george.hideturtle()
    createSquares(screen, ['black', 'white'])
    
    glider = [(1, 3), (2, 3), (3, 3), (3, 2), (2, 1)]
    grid = life(rows, columns, 200, glider, george)
    
    screen.update()
    screen.exitonclick()
    
main()
