from math import cos
from math import pi

class Function:
	def __init__(self):
		self.function = None
		self.min=-0.0
		self.max=0.0

class Rosenbrock(Function):
	def __init__(self, min=-5.0, max=5.0):
		self.function="(1.0-x)+100.0*(y-x**2)*(y-x**2)"
		self.min=min
		self.max=max

class Rastrigin(Function):
	def __init__(self, min=-5.12, max=5.12):
		self.function="20 + x**2 + y**2 - (10*math.cos(2 * math.pi * x)) - (10*math.cos(2 * math.pi * y))"
		self.min=min
		self.max=max
