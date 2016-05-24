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


from springpython.context import ApplicationContext

from GeneticComponents import *

if __name__ == "__main__":
	applicationContext = ApplicationContext(GeneticComponents()) # albo XMLConfig("GeneticComponents.xml")

	population = applicationContext.get_object("population")
	population.setMin(-30)
	population.setMax(30)
	generator = applicationContext.get_object("generator")
	operators = applicationContext.get_objects_by_type(Operator, False)
	stop_condition = applicationContext.get_object("stop_condition")
	
	selection=applicationContext.get_object("selection")
	evaluation=applicationContext.get_object("evaluation")
	crossover=applicationContext.get_object("crossover")
	mutation=applicationContext.get_object("mutation")

	population=generator.generate(population, "x+y", 100, -30., 30.)
    #population.printPopulation()
    
    #generator.setRastrigin(population)
	generator.setRosenbrock(population)

	evaluation.evaluation(population)

for i in xrange(0, 5):
		
#print "old"
#population.printPopulation()
		newGenotypes=[]
		for pos in range(0, population.getSize()/2):
            #populacja, rozmiar po selekcji, rozmiar losowanych jednostek ( z nich bedzie brany najlepszy i dodawany do nowej populacji)
			selectionPopulation=selection.tournament(population, 5, 10)
            #selectionPopulation=selection.roulette(population)
			newTwoGenotypes=crossover.crossover(population, selectionPopulation, 0.5)
			newGenotypes.append(newTwoGenotypes[0])
			newGenotypes.append(newTwoGenotypes[1])
			
		population.setGenotypes(newGenotypes)
		mutation.mutation(population, 0.1, 0.6)

		print "new"
		population.printPopulation()
