from Operator import *
import math

class Evaluation(Operator):
	def evaluation(self, population):
		print("Ocena osobnikow")

		for genotype in population.getGenotypes():
			x=genotype.value[0]
			y=genotype.value[0]
			genotype.setFitness(eval(population.getFitness()))