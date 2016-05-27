from random import Random

from Operator import *

class Selection(Operator):
	def __init__(self, newSize=None, probeSize=None):
		self.newSize = newSize;
		self.probeSize = probeSize;

	def operate(self, population):
		selectionPopulation=[]
		random = Random()

		if (self.newSize>=len(population.getGenotypes())):
			return population.getGenotypes()

		for x in xrange(0,self.newSize):
			tempPopulation=[]
			for y in xrange(0,self.probeSize):
				newGen=population.getGenotypes()[random.randint(0, len(population.getGenotypes())-1)]
				while newGen in selectionPopulation:
					newGen=population.getGenotypes()[random.randint(0, len(population.getGenotypes())-1)]

				tempPopulation.append(newGen)
			selectionPopulation.append(self.best(tempPopulation))

		return selectionPopulation

	def best(self, population):
		pos=0
		bestPos=0
		best=population[0].getFitness()

		for genotype in population:
			if genotype.getFitness()>best:
				best=genotype.getFitness()
				bestPos=pos

			pos=pos+1
		return population[bestPos]

	def minimum(self, population):
		min=None
		for genotype in population.getGenotypes():
			if min>genotype.getFitness() or min==None:
				min=genotype.getFitness()
		return min


	def sum(self, population):
		sum=0
		for genotype in population.getGenotypes():
			if min>genotype.getFitness():
				sum=sum+genotype.getFitness()
		return sum

	def roulette(self, population):
		print "Selekcja ruletkowa"
		random = Random()
		worstValue=self.minimum(population)
		sumValue=self.sum(population)
		selectionPopulation=[]

		for genotype in population.getGenotypes():
			if random.uniform(0, 1)<=(worstValue-genotype.getFitness()+1)/(sumValue+1):
				selectionPopulation.append(genotype)
		return selectionPopulation
