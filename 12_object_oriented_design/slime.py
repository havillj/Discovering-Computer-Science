"""
Project 12.3
Slime class

Discovering Computer Science, Second Edition
Jessen Havill
"""

import turtle
import random, math

SNIFF_THRESHOLD = 1.0   # level at which slime mold amoeboid moves toward chemical (cAMP)
WIGGLE_ANGLE = 40.0     # maximum random wiggle angle
SNIFF_ANGLE = 45.0      # angle to sniff left and right
SNIFF_DIST = 1.0        # distance able to sniff ahead
MOVE_DIST = 1.0         # distance moved in one tick

def roundPosition(pos):
	return (round(pos[0]), round(pos[1]))

class Slime:

	def __init__(self):
		pass
		
	def go(self):
		pass
