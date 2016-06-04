from math import fabs

class StopCondition:
	def __init__(self, diff_const=0.1):
		self.previous_generation_fitness = 0.0
		self.diff_const = diff_const
		self.lapsed_iterations = 0

	def stop(self, population):
		if fabs(self.previous_generation_fitness - population.meanFitness()) < self.diff_const:
			return True
		else:
			self.previous_generation_fitness = population.meanFitness()
			self.lapsed_iterations = self.lapsed_iterations + 1
			return False