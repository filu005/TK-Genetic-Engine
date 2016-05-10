from Operator import *

class Evaluation(Operator):
	def operate(self, population):
		print "evaluation"

	def evaluation():
		print("Ocena osobnikow")

		for genotype in population:
			x=genotype.value
			genotype.setfitness(eval(function))