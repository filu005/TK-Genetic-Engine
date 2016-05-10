class Population:
    self.id
    # lista genotypów (?)
    self.genotypes=[]

    def setid(self, id):
        self.id=id

    def getid(self, id):
        return self.id

	# returns finds genotype with highest fitness
	def getBestGenotype():
		Genotype best = genotypes.value[0]
		for it in genotypes:
			if it.get_fitness() > best.get_fitness():
				best = it
		return best