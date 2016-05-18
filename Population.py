from Genotype import *

class Population:
    def setId(self, id):
        self.id=id

    def getId(self, id):
        return self.id

    def getSize(self):
        return self.size
        
    def setSize(self, size):
        self.size=size
        
    def getFitness(self):
        return self.fitness
        
    def setFitness(self, fitness, min, max):
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
    
    def __init__(self):
        self.id=None
        self.genotypes=[]
        self.size=None
        self.fitness=None
        self.min=None
        self.max=None
    
    def printPopulation(self):
        for x in range(0,self.getSize()):
            print "Genotyp: "+str(self.getGenotypes()[x].getValue())
            print "Wartosc fitness: "+str(self.getGenotypes()[x].getFitness())

        
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