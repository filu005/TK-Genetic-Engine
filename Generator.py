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
  
  xCenter=random.uniform(min, max)
  yCenter=random.uniform(min, max)
  
  for x in range(0, size):
   y=None
   x=None
   while x==None or x<min or x>max:
    x=xCenter*random.random()*max/5-min/5

   while y==None or y<min or y>max:
    y=yCenter*random.random()*max/5-min/5

   
   genotypes.append(Genotype([x,y]))
  
  
  population.setSize(size)
  population.setGenotypes(genotypes)
  population.setFitness(function, min, max)
  print len(genotypes)
 
  return population
