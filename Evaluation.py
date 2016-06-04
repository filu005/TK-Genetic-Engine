from Operator import *
import math

class Evaluation(Operator):
	def operate(self, population):
		# for genotype in population.getGenotypes():
		for idx in xrange(0, population.getSize()):
			x=population.genotypes[idx].value[0]
			y=population.genotypes[idx].value[1]
			# evaluate fitness value for every genotype
			population.genotypes[idx].setFitness(eval(population.getFitnessFunction()))