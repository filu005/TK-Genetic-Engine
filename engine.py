from random import Random
from time import time
from math import cos
from math import pi

class Engine:

	xrange=None
	yrange=None
	function=None
	population=[]

	def setxrange(range):
		self.xrange=range

	def setyrange(range):
		self.yrange=range

	def setfunction(self, function, xrange, yrange):
		print("Zmiana funckji fitnes na "+function)
		self.function=function
		self.xrange=xrange
		self.yrange=yrange

	def getfunction():
		return self.function

	def generate_function(self, random, size):
		return [random.uniform(-5.12, 5.12) for i in xrange(size)]

	def evaluate_rastrigin(self, candidates):
		fitness = []
		for cs in candidates:
			fit = [eval(function) for x in cs]
			fitness.append(fit)
		return fitness

	def initializeF(self, function):
		if function=="Rosenbrock":
			function="(1-x)+100*(y-x**)*(y-x**)"
			xrange=-30.
			yrange=30.
		elif function=="Rastrigin":
			function="10 * len(cs) + sum([((x - 1)**2 - 10 * cos(2 * pi * (x - 1)))"
			xrange=-5.12
			yrange=5.12

		self.initialize(function, xrange, yrange)

	def initialize(self, function, xrange, yrange):
		rand = Random()
		rand.seed(int(time()))
		self.setfunction(function, xrange, yrange)

from springpython.context import ApplicationContext

from GeneticComponents import *

if __name__ == "__main__":
	applicationContext = ApplicationContext(GeneticComponents()) # albo XMLConfig("GeneticComponents.xml")

	generator = applicationContext.get_object("generator")
	population = generator.generate()
	operators = applicationContext.get_objects_by_type(Operator, False)
	stop_condition = applicationContext.get_object("stop_condition")

	while stop_condition.stop(population) == False:
		for it in operators:
			operators[it].operate(population)
