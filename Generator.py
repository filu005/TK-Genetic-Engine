from Genotype import Genotype
from Population import Population

from random import Random
class Generator:
	def __init__(self, function, size, min, max):
		self.function = function
		self.size = size
		self.min = min
		self.max = max

	def setRosenbrock(self, population):
		function="(1-x)+100*(y-x**2)*(y-x**2)"
		min=-30.
		max=30.
		population.setFitness(function, min, max)


	def setRastrigin(self, population):
		function="10 * population.getSize() + sum([((x - 1)**2 - 10 * math.cos(2 * math.pi * (x - 1)))])"
		min=-5.12
		max=5.12
		population.setFitness(function, min, max)

	def generate(self):
		print ("Generowanie populacji")
		population = Population()
		random=Random()
		genotypes=[]

		xCenter=random.uniform(self.min, self.max)
		yCenter=random.uniform(self.min, self.max)

		for x in range(0, self.size):
			y=None
			x=None

			while x==None or x<self.min or x>self.max:
				x=xCenter*random.random()*self.max/5-self.min/5

			while y==None or y<self.min or y>self.max:
				y=yCenter*random.random()*self.max/5-self.min/5

			genotypes.append(Genotype([x,y]))

		population.setSize(self.size)
		population.setGenotypes(genotypes)
		population.setFitness(self.function, self.min, self.max)
		print len(genotypes)

		return population
