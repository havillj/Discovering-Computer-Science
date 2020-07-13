"""
Project 12.3
Slime world class

Discovering Computer Science, Second Edition
Jessen Havill
"""

import turtle
from patch import *

WIN_SCALE = 6          # amount to scale window by; each patch will be this long on a side

class World:

	def __init__(self, iwidth, iheight):
		self.tick = 0
		self.width = iwidth
		self.height = iheight
		self.scale = WIN_SCALE
			
		self.worldTurtle = turtle.Turtle()
		self.worldScreen = self.worldTurtle.getscreen()
		self.worldScreen.setup(self.width * self.scale + 20, self.height * self.scale + 20)
		self.worldScreen.setworldcoordinates(0, 0, self.width - 1, self.height - 1)
		self.worldTurtle.hideturtle()
		self.worldTurtle.up()
		self.worldTurtle.speed(0)
		
		self.patchesImg = turtle.TK.PhotoImage(height = self.height * self.scale, width = self.width * self.scale)
		id = self.worldScreen._canvas.create_image(self.width * self.scale / 2, -self.height * self.scale / 2, image = self.patchesImg)

	def update(self):
		"""Update the background image of chemical levels.  Call this once per tick."""
		
		for pos in self.grid:
			self.grid[pos].draw()
