from Genotype import *

class Population:
	def __init__(self):
		self.id=None
		self.genotypes=[]
		self.size=None
		self.fitness=None
		self.min=None
		self.max=None

	def printPopulation(self):
		return_string = ""
		for x in range(0,self.size):
			return_string += "Genotyp: " + str(self.getGenotypes()[x].getValue())
			return_string += "\n"
			return_string += "Wartosc fitness: " + str(self.getGenotypes()[x].getFitness())
			return_string += "\n"
		return return_string

	def setId(self, id):
		self.id=id

	def getId(self, id):
		return self.id

	def getSize(self):
		return self.size

	def setSize(self, size):
		self.size=size

	def getFitnessFunction(self):
		return self.fitness

	def setFitnessFunction(self, fitness, min, max):
		self.fitness=fitness
		self.setMin(min)
		self.setMax(max)

	def getGenotypes(self):
		return self.genotypes

	def setGenotypes(self, genotypes):
		self.genotypes=genotypes

	def getMin(self):
		return self.min

	def setMin(self, min):
		self.min=min

	def getMax(self):
		return self.max

	def setMax(self, max):
		self.max=max

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

	def meanFitness(self):
		sumfit = 0.0
		for genotype in self.genotypes:
			sumfit = sumfit + genotype.getFitness()
		return (sumfit / self.size)

	# returns finds genotype with highest fitness
	def getBestGenotype():
		if getSize()>0:
			best = genotypes[0]
			for it in genotypes:
				if it.get_fitness() > best.get_fitness():
					best = it
			return best
		else:
			return 0
