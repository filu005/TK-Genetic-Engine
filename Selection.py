from random import Random

from Operator import *

class Selection(Operator):
	def operate(self, population):
		print "selection" + " in population " + population

	def roulette(self):
		random = Random()
		worstValue=min(self)
		sumValue=self.sum()

		for genotype in population:
			if random.uniform(0, 1)>(worstValue-genotype.getvalue()+1)/(sumValue+1):
				self.population.remove(genotype)

	def tournament(self):
		newPopulation=[]
		random = Random()

		for x in xrange(0,int(population/3)):
			tempPopulation=[]
			for y in xrange(0,int(population/3)):
				tempPopulation.append(population[random.randint(0, len(population))])
			newPopulation.append(best(tempPopulation))

		population=newPopulation

	def best(population):
		pos=0
		bestPos=0
		best=population[0].getvalue()

		for genotype in population:
			if genotype.getvalue()<best:
				best=genotype.getvalue()
				bestPos=pos

			pos=pos+1

		return population[bestPos]

	def min(self):
		min=None
		for genotype in population:
			if min>genotype.getvalue():
				min=genotype.getvalue()
		return min


	def sum(self):
		sum=0
		for genotype in population:
			if min>genotype.getvalue():
				sum=sum+genotype.getvalue()
		return sum
