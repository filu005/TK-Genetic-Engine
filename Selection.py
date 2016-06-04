from random import Random
from copy import deepcopy

from Operator import *

class Selection(Operator):
	def __init__(self, tournamentSelectionSize=None):
		self.tournamentSelectionSize = tournamentSelectionSize;

	def operate(self, population):
		selectionPopulation=[]
		random=Random()
		random.seed()

		# petla trwa dopoki nie osiagnieta zostanie nowa
		# populacja o liczebnosci populacji identycznej do tej
		# z ktorej wybierane sa osobniki (pop. z poprzedniej generacji).
		# to taka symulacja petli do...until
		while 1:
			bestGenotype = None
			bestFitness = 1000000
			# losujemy tournamentSelectionSize wartosci
			# do grupy turniejowej
			for i in xrange(0,self.tournamentSelectionSize):
				selection_idx = random.randint(0, population.getSize()-1)
				if population.genotypes[selection_idx].fitness < bestFitness:
					bestFitness = population.genotypes[selection_idx].fitness
					bestGenotype = deepcopy(population.genotypes[selection_idx])

			# najlepszegpp zawodnika z grupy wsadzamy do
			# nowej populacji
			if bestGenotype != None:
				selectionPopulation.append(bestGenotype)

		# ...until
			if len(selectionPopulation) == len(population.genotypes):
				break

		population.setGenotypes(selectionPopulation)

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
		random.seed()
		worstValue=self.minimum(population)
		sumValue=self.sum(population)
		selectionPopulation=[]

		for genotype in population.getGenotypes():
			if random.uniform(0, 1)<=(worstValue-genotype.getFitness()+1)/(sumValue+1):
				selectionPopulation.append(genotype)
		return selectionPopulation
