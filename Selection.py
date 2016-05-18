from random import Random

from Operator import *

class Selection(Operator):
	def operate(self, population):
		print "selection" + " in population " + population

	def best(self, population):
		pos=0
		bestPos=0
		best=population[0].getValue()

		for genotype in population:
			if genotype.getValue()<best:
				best=genotype.getValue()
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
			if min>genotype.getValue():
				sum=sum+genotype.getValue()
		return sum

	def roulette(self, population):
		print "Selekcja ruletkowa"
		random = Random()
		worstValue=self.minimum(population)
		sumValue=self.sum(population)

		for genotype in population.getGenotypes():
			if random.uniform(0, 1)>(worstValue-genotype.getFitness()+1)/(sumValue+1):
				population.getGenotypes().remove(genotype)
		print "Rozmiar po selekcji ruletkowej: "+str(len(population.getGenotypes()))


	def tournament(self, population, newSize, probeSize):
		newPopulation=[]
		random = Random()

		for x in xrange(0,newSize):
			tempPopulation=[]
			for y in xrange(0,probeSize):
				tempPopulation.append(population.getGenotypes()[random.randint(0, len(population.getGenotypes())-1)])
			newPopulation.append(self.best(tempPopulation))

		population.setGenotypes(newPopulation)
		print "Rozmiar po selekcji turniejowej: "+str(len(population.getGenotypes()))

