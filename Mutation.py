from Operator import *
import numpy as np

class Mutation(Operator):
    # pm - wspolczynnik mutacji (0.6 np)
    def mutation(self, population, prob, pm):
        print "mutation"
        for genotype in population.getGenotypes():
            if prob>=np.random.random():
                x=genotype.getValue()[0]
                y=genotype.getValue()[1]
                
                xGen=x+float(pm-np.random.randn())*x
                yGen=y+float(pm-np.random.randn())*y


                if xGen<population.getMin():
                    xGen=population.getMin()
                elif xGen>population.getMax():
                    xGen=population.getMax()

                genotype.setValue([xGen, yGen])

