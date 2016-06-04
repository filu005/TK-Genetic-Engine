from Genotype import Genotype
from Population import Population

from random import Random
class Generator:
	def __init__(self, function, population_size):
		self.function = function.function
		self.size = population_size
		self.min = function.min
		self.max = function.max

	def generate(self):
		print ("Generowanie populacji")
		population = Population()
		random=Random()
		random.seed()
		genotypes=[]

		xCenter=random.uniform(self.min, self.max)
		yCenter=random.uniform(self.min, self.max)

		for i in range(0, self.size):
			# y=None
			# x=None
			x=random.uniform(self.min, self.max)
			y=random.uniform(self.min, self.max)

			# while x==None or x<self.min or x>self.max:
			# 	x=xCenter*random.random()*self.max/5-self.min/5

			# while y==None or y<self.min or y>self.max:
			# 	y=yCenter*random.random()*self.max/5-self.min/5

			genotypes.append(Genotype([x,y]))

		population.setSize(self.size)
		population.setGenotypes(genotypes)
		population.setFitnessFunction(self.function, self.min, self.max)
		print len(genotypes)

		return population
