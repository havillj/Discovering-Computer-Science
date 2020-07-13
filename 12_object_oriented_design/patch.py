"""
Project 12.3
Patch class

Discovering Computer Science, Second Edition
Jessen Havill
"""

CHEMICAL_ADD = 2.0        # units of chemical (cAMP) dropped by slime at each step
EVAPORATION_RATE = 0.9    # reduction in chemical levels each tick

class Patch:

	def __init__(self, ipos, iworld):
		self.pos = ipos
		self.chemical = 0
		self.world = iworld
		
	def draw(self):
		c = max(0, 255 - (85 * self.chemical))
		cx = '#{:02x}ff{:02x} '.format(c, c)
		scale = self.world.getScale()
		square = ('{' + cx * scale + '} ') * scale
		self.world.patchesImg.put(square, (self.pos[0] * scale, self.world.patchesImg.height() - (self.pos[1] + 1) * scale))
