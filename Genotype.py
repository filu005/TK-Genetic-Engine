class Genotype:

    def __init__(self, value):
        self.fitness=None
        self.value=value

    def setFitness(self, fitness):
        self.fitness=fitness

    def getFitness(self):
        return self.fitness

    def getValue(self):
        return self.value

    def setValue(self, fitness):
        self.value=value