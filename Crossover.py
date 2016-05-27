from Operator import *
import numpy as np

class Crossover(Operator):
	def __init__(self, pc=None):
		self.pc = pc

	def operate(self, population, selection):
		genotypesNew=[]
		genotypes=population.getGenotypes()

		print "Selekcja"

		if self.pc>=np.random.random() and len(selection)>0:
			genotypesNew.append(self.best(selection))
			genotypesNew.append(self.second(selection))
		else:
			genotypesNew.append(genotypes[0])
			genotypesNew.append(genotypes[1])


		self.remove(genotypes, genotypesNew[0])
		self.remove(genotypes, genotypesNew[1])

		return genotypesNew


	def best(self, population):
		pos=0
		bestPos=0
		best=population[0].getFitness()

		for genotype in population:
			if genotype.getFitness()<best:
				best=genotype.getFitness()
				bestPos=pos
				pos=pos+1

		return population[bestPos]


	def bestPos(self, population):
		pos=0
		bestPos=0
		best=population[0].getFitness()

		for genotype in population:
			if genotype.getFitness()<best:
				best=genotype.getFitness()
				bestPos=pos
				pos=pos+1

		return bestPos


	def second(self, population):
		pos=0
		bestPos=0
		best=population[0].getValue()
		bestP=self.bestPos(population)

		if bestPos==bestP:
			bestPos=bestPos+1

		for genotype in population:
			if genotype.getValue()<best and pos!=bestP:
				best=genotype.getValue()
				bestPos=pos
				pos=pos+1

		return population[bestPos]


	def remove(self, genotypes, object):
		for x in genotypes:
			if x.getFitness()==object.getFitness():
				genotypes.remove(x)
				return
