from Operator import *
from random import Random
import numpy as np

class Mutation(Operator):
    def __init__(self, prob=None, pm=None):
        self.prob = prob;
        self.pm = pm;

    def operate(self, population):
        random=Random()
        random.seed()
        # for genotype in population.getGenotypes():
        for idx in xrange(0, population.getSize()):
            if self.prob>=np.random.random():
                x=population.genotypes[idx].getValue()[0]
                y=population.genotypes[idx].getValue()[1]

                # xGen=x*self.pm+float(self.pm-np.random.randn())*x
                # yGen=y*self.pm+float(self.pm-np.random.randn())*y

                xGen=x*random.uniform(1.0-self.pm, 1.0+self.pm)
                yGen=y*random.uniform(1.0-self.pm, 1.0+self.pm)

                if xGen<population.getMin():
                    xGen=population.getMin()
                elif xGen>population.getMax():
                    xGen=population.getMax()

                if yGen<population.getMin():
                    yGen=population.getMin()
                elif yGen>population.getMax():
                    yGen=population.getMax()

                population.genotypes[idx].setValue([xGen, yGen])

