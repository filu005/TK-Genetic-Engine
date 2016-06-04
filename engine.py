from random import Random
from time import time
from math import cos
from math import pi

from springpython.context import ApplicationContext

from GeneticComponents import *

if __name__ == "__main__":
	applicationContext = ApplicationContext(GeneticComponents()) # albo XMLConfig("GeneticComponents.xml")

	generator = applicationContext.get_object("generator")
	stop_condition = applicationContext.get_object("stop_condition")

	selection=applicationContext.get_object("selection")
	evaluation=applicationContext.get_object("evaluation")
	crossover=applicationContext.get_object("crossover")
	mutation=applicationContext.get_object("mutation")

	population=generator.generate()
	evaluation.operate(population)

	# print population.printPopulation()

	while stop_condition.stop(population) == False:
		evaluation.operate(population)
		selection.operate(population)
		crossover.operate(population)
		mutation.operate(population)

	# do drukowania poprawnych wynikow
	# jeszcze raz licze fitness
	evaluation.operate(population)
	outs = "-- finish after " + repr(stop_condition.lapsed_iterations) + " iterations --"
	print population.printPopulation()
	print outs
