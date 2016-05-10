from random import Random
from time import time
from math import cos
from math import pi

class Engine:

	xrange=None
	yrange=None
	function=None
	population=[]

	def setxrange(range):
		self.xrange=range

	def setyrange(range):
		self.yrange=range

	def setfunction(self, function, xrange, yrange):
		print("Zmiana funckji fitnes na "+function)
		self.function=function
		self.xrange=xrange
		self.yrange=yrange

	def getfunction():
		return self.function

	def generate_function(self, random, size):
		return [random.uniform(-5.12, 5.12) for i in xrange(size)]

	def evaluate_rastrigin(self, candidates):
		fitness = []
		for cs in candidates:
			fit = [eval(function) for x in cs]
			fitness.append(fit)
		return fitness

	def generate(self, random, size):
		return [random.uniform(-30., 30.) for i in xrange(size)]


	def initializeF(self, function):
		if function=="Rosenbrock":
			function="(1-x)+100*(y-x**)*(y-x**)"
			xrange=-30.
			yrange=30.
		elif function=="Rastrigin":
			function="10 * len(cs) + sum([((x - 1)**2 - 10 * cos(2 * pi * (x - 1)))"
			xrange=-5.12
			yrange=5.12

		self.initialize(function, xrange, yrange)


	def initialize(self, function, xrange, yrange):
		rand = Random()
		rand.seed(int(time()))
		self.setfunction(function, xrange, yrange)


	def evaluation():
		print("Ocena osobnikow")

		for genotype in population:
			x=genotype.value
			genotype.setfitness(eval(function))


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


	def tournament(self):
		newPopulation=[]
		random = Random()

		for x in xrange(0,int(population/3)):
			tempPopulation=[]
			for y in xrange(0,int(population/3)):
				tempPopulation.append(population[random.randint(0, len(population))])
			newPopulation.append(best(tempPopulation))

		population=newPopulation


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



	def roulette(self):
		random = Random()
		worstValue=min(self)
		sumValue=self.sum()

		for genotype in population:
			if random.uniform(0, 1)>(worstValue-genotype.getvalue()+1)/(sumValue+1):
				self.population.remove(genotype)


	def selection(type):

		print("Selekcja")
		if type=="tournament":
			self.tournament()
		elif type=="roulette":
			self.roulette()


	def crossover(p):
		print("Krzyzwanie")

	def mutation(p):
		print("Mutacja")



engine=Engine()
engine.initialize("x+2", 10, 10)

