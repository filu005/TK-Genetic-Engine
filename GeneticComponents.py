from springpython.config import Object
from springpython.context import scope
from springpython.config import PythonConfig

from Generator import *
from StopCondition import *
from Evaluation import *
from Selection import *
from Crossover import *
from Mutation import *
from Population import *

class GeneticComponents(PythonConfig):
	def __init__(self):
		super(GeneticComponents, self).__init__()

	@Object
	def generator(self):
		return Generator("x+y", 100, -30.0, 30.0)

	@Object
	def stop_condition(self):
		return StopCondition()

	@Object(scope.SINGLETON, abstract=False)
	def selection(self):
		return Selection(5, 10)

	@Object(scope.SINGLETON, abstract=False)
	def evaluation(self):
		return Evaluation()

	@Object(scope.SINGLETON, abstract=False)
	def crossover(self):
		return Crossover(pc=0.5) # pc - wspolczynnik krzyzowania

	@Object(scope.SINGLETON, abstract=False)
	def mutation(self):
		return Mutation(prob=0.1, pm=0.6)

	@Object
	def population(self):
		return Population()
