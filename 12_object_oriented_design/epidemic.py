"""
Augmented epidemic simulation from Section 12.1

Discovering Computer Science, Second Edition
Jessen Havill
"""

import turtle
from world import *
import tkinter as tk
import matplotlib.pyplot as pyplot
from matplotlib.backends.backend_tkagg import FigureCanvas

WIDTH = 600
HEIGHT = 600

def go():
    infectionProbability = infectionScale.get()  # get slider values
    numberPeople = peopleScale.get()
    
    worldScreen.clear()     # reset the turtle graphics screen
    worldScreen.tracer(0)
    
    world = World(WIDTH, HEIGHT, infectionProbability, numberPeople, worldScreen)
    
    figure.clear()                          # reset the plot
    graph = figure.add_subplot()
    graph.set_xlabel('Simulation steps')
    graph.set_ylabel('Number infected')
    graph.set_ylim(0, numberPeople)
    lines, = graph.plot([0], [1], color = 'blue')
        
    time = 0
    numberInfected = [1]
    while world.getNumberInfected() != numberPeople:  # loop until all are infected
        world.stepAll()
        worldScreen.update()
        time = time + 1
        numberInfected.append(world.getNumberInfected())
        
        if time % 10 == 0:   # update the plot every 10 steps
            lines.set_data(range(time + 1), numberInfected)
            graph.set_xlim(0, time + 1)
            figure.canvas.draw()
            
    figure.canvas.draw()  # update plot one last time at the end

def main():
    global worldScreen, infectionScale, peopleScale, figure
    
    root = tk.Tk()     # tkinter root window

    # canvas for turtle graphics
    simulationCanvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, 
                                 relief = tk.SUNKEN, borderwidth = 2)
    simulationCanvas.grid(row = 0, column = 0)
    worldScreen = turtle.TurtleScreen(simulationCanvas)
    worldScreen.setworldcoordinates(0, 0, WIDTH - 1, HEIGHT - 1)
    
    # canvas for the plot
    figure = pyplot.Figure(figsize = (WIDTH / 100, HEIGHT / 100), dpi = 100)
    graph = figure.add_subplot()
    graph.set_xlabel('Simulation steps')
    graph.set_ylabel('Number infected')
    plotCanvas = FigureCanvas(figure, master = root)
    plotCanvas.get_tk_widget().grid(row = 0, column = 1)

    # slider for infection probability
    infectionProbability = tk.DoubleVar()
    infectionScale = tk.Scale(root, orient = tk.HORIZONTAL, label = 'Infection probability', 
                              length = WIDTH - 50, from_ = 0.0, to = 1.0, resolution = 0.01, 
                              tickinterval = 0.1, variable = infectionProbability)
    infectionScale.grid(row = 1, column = 0, pady = 10)

    # slider for the number of people
    numberPeople = tk.IntVar()
    peopleScale = tk.Scale(root, orient = tk.HORIZONTAL, label = 'Number of people', 
                              length = WIDTH - 50, from_ = 0, to = 500, resolution = 1, 
                              tickinterval = 100, variable = numberPeople)
    peopleScale.grid(row = 2, column = 0, pady = 10)

    # "Go" button
    goButton = tk.Button(root, text = 'Go', width = 10, command = go)
    goButton.grid(row = 2, column = 1)
    
    root.mainloop()
    
main()
