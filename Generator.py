from Genotype import Genotype

from random import Random
class Generator:
 
 def setRosenbrock(self, population):
  function="(1-x)+100*(y-x**2)*(y-x**2)"
  min=-30.
  max=30.
  population.setFitness(function, min, max)
   
  
 def setRastrigin(self, population):
  function="10 * population.getSize() + sum([((x - 1)**2 - 10 * math.cos(2 * math.pi * (x - 1)))])"
  min=-5.12
  max=5.12
  population.setFitness(function, min, max)

 def generate(self, population, function, size, min, max):
  print ("Generowanie populacji")
  random=Random()
  genotypes=[]
  
  for x in range(0, size):
   genotypes.append(Genotype([random.uniform(min, max),random.uniform(min, max)]))
  
  
  population.setSize(size)
  population.setGenotypes(genotypes)
  population.setFitness(function, min, max)
  print len(genotypes)
 
  return population
