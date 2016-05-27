from Operator import *
import numpy as np

class Mutation(Operator):
    def __init__(self, prob=None, pm=None):
        self.prob = prob;
        self.pm = pm;

    # pm - wspolczynnik mutacji (0.6 np)
    def operate(self, population):
        print "mutation"
        for genotype in population.getGenotypes():
            if self.prob>=np.random.random():
                x=genotype.getValue()[0]
                y=genotype.getValue()[1]

                xGen=x*self.pm+float(self.pm-np.random.randn())*x
                yGen=y*self.pm+float(self.pm-np.random.randn())*y


                if xGen<population.getMin():
                    xGen=population.getMin()
                elif xGen>population.getMax():
                    xGen=population.getMax()

                if yGen<population.getMin():
                    yGen=population.getMin()
                elif yGen>population.getMax():
                    yGen=population.getMax()

                genotype.setValue([xGen, yGen])

