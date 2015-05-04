"""
Represent various videogame controllers

TODO: Various play schemes/configs
XXX: UNTESTED
"""

import re

def setup_controls(joystick):
	"""
	Joystick wrapper.
	"""
	name = joystick.get_name()
	axes = joystick.get_numaxes()
	btns = joystick.get_numbuttons()
	if re.search('playstation', name, re.I):
		return Ps3Controller(joystick)

	elif re.search('X-box', name, re.I):
		return XboxController(joystick)

	elif re.search('Thrustmaster dual analog 3.2', name, re.I):
		return MyThrustController(joystick)

	elif re.search('Gamepad F310', name, re.I):
		return MyF310Controller(joystick)

	# this should also match generic 4-axis, 12 button dual stick
	elif re.search('Saitek', name, re.I) or ( axes == 4 and btns == 12 ):
		return MySaitekController(joystick)
	
	return Controller(joystick)

class Controller(object):

	def __init__(self, joystick):
		"""Pass a PyGame joystick instance."""
		self.js = joystick

	def getLeftHori(self):
		return self.js.get_axis(0)

	def getLeftVert(self):
		return self.js.get_axis(1)

	def getRightHori(self):
		return self.js.get_axis(2)

	def getRightVert(self):
		return self.js.get_axis(3)

	def getLeftTrigger(self):
		return self.js.get_axis(4)

	def getRightTrigger(self):
		return self.js.get_axis(5)

class XboxController(Controller):

	def __init__(self, joystick):
		super(XboxController, self).__init__(joystick)

	def getLeftHori(self):
		return self.js.get_axis(0)

	def getLeftVert(self):
		return self.js.get_axis(1)

	def getRightHori(self):
		return self.js.get_axis(3)

	def getRightVert(self):
		return self.js.get_axis(4)

	def getLeftTrigger(self):
		return self.js.get_axis(2)

	def getRightTrigger(self):
		return self.js.get_axis(5)

class Ps3Controller(Controller):

	def __init__(self, joystick):
		super(Ps3Controller, self).__init__(joystick)

	def getLeftHori(self):
		return self.js.get_axis(0)

	def getLeftVert(self):
		return self.js.get_axis(1)

	def getRightHori(self):
		return self.js.get_axis(2)

	def getRightVert(self):
		return self.js.get_axis(3)

	def getLeftTrigger(self):
		# TODO: Verify
		return self.js.get_axis(12)

	def getRightTrigger(self):
		# TODO: Verify
		return self.js.get_axis(13)

# This also works for
# USB Controller - 4 axis - 12 button - generic 4 axis dual stick controller
class MySaitekController(Controller):

	def __init__(self, joystick):
		super(MySaitekController, self).__init__(joystick)

	def getLeftHori(self):
		return self.js.get_axis(0)

	def getLeftVert(self):
		return self.js.get_axis(1)

	def getRightHori(self):
		return self.js.get_axis(3)

	def getRightVert(self):
		return self.js.get_axis(2)

	def getLeftTrigger(self):
		return self.js.get_button(6)

	def getRightTrigger(self):
		return self.js.get_button(7)

class MyThrustController(Controller):

	def __init__(self, joystick):
		super(MyThrustController, self).__init__(joystick)

	def getLeftHori(self):
		return self.js.get_axis(0)

	def getLeftVert(self):
		return self.js.get_axis(1)

	def getRightHori(self):
		return self.js.get_axis(2)

	def getRightVert(self):
		return self.js.get_axis(3)

	def getLeftTrigger(self):
		return self.js.get_button(5)

	def getRightTrigger(self):
		return self.js.get_button(7)

class MyF310Controller(Controller):

	def __init__(self, joystick):
		super(MyF310Controller, self).__init__(joystick)

	def getLeftHori(self):
		return self.js.get_axis(0)

	def getLeftVert(self):
		return self.js.get_axis(1)

	def getRightHori(self):
		return self.js.get_axis(4)

	def getRightVert(self):
		return self.js.get_axis(3)

	def getLeftTrigger(self):
		return self.js.get_button(4)

	def getRightTrigger(self):
		return self.js.get_button(5)
