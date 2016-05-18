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
		return Generator()

	@Object
	def stop_condition(self):
		return StopCondition()

	@Object
	def selection(self):
		return Selection()

	@Object
	def evaluation(self):
		return Evaluation()

	@Object
	def crossover(self):
		return Crossover()

	@Object
	def mutation(self):
		return Mutation()

	@Object
	def population(self):
		return Population()
