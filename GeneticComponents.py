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
from Functions import *

class GeneticComponents(PythonConfig):
	def __init__(self):
		super(GeneticComponents, self).__init__()

	# function - funkcja zddefiniowana jako implementacja klasy Function
	# population_size - rozmiar populacji
	@Object
	def generator(self):
		return Generator(function=Rastrigin(-5.12, 5.12), population_size=50)

	# diff_const - wspolczynnik roznicy sredniej funkcji dostosowania
	# 	pomiedzy generacjami wymagany do zakonczenia algorytmu
	@Object
	def stop_condition(self):
		return StopCondition(diff_const=0.001)

	# tournamentSelectionSize - ilosc osobnikow w grupie turniejowej
	@Object(scope.SINGLETON)
	def selection(self):
		return Selection(tournamentSelectionSize=10)

	@Object(scope.SINGLETON)
	def evaluation(self):
		return Evaluation()

	# pc - wspolczynnik krzyzowania
	@Object(scope.SINGLETON)
	def crossover(self):
		return Crossover(pc=0.02)

	# prob - prawdopodobienstwo mutacji
	# pm - wspolczynnik mutacji
	@Object(scope.SINGLETON)
	def mutation(self):
		return Mutation(prob=0.1, pm=0.01)
