from Operator import *
import numpy as np

class Crossover(Operator):
	def __init__(self, pc=None):
		self.pc = pc

	def operate(self, population):
		for p1_idx in xrange(1, population.getSize()-1):
			p2_idx=0
			if p1_idx%2==0:
				p2_idx=p1_idx-1
			else:
				p2_idx=p1_idx+1
			# print p1_idx
			# jesli bedzie crossover
			if self.pc >= np.random.random():
				# podmien wartosci x
				if np.random.random() > 0.5:
					temp=population.genotypes[p1_idx].getValue()[0]
					population.genotypes[p1_idx].value[0] = population.genotypes[p2_idx].value[0]
					population.genotypes[p2_idx].value[0]=temp
				# podmien wartosci y
				else:
					temp=population.genotypes[p1_idx].value[1]
					population.genotypes[p1_idx].value[1] = population.genotypes[p2_idx].value[1]
					population.genotypes[p2_idx].value[1]=temp

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
