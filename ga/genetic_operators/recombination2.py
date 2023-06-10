from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual import Individual
from ga.genetic_operators.recombination import Recombination

class Recombination2(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)
    #Recombination Cycle Crossover (CX):
    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        num_genes = ind1.num_genes
        cycle = [False] * num_genes
        child1 = [-1] * num_genes
        child2 = [-1] * num_genes

        # Perform the cycle crossover
        index = 0
        while not cycle[index]:
            cycle[index] = True
            child1[index] = ind1.genome[index]
            child2[index] = ind2.genome[index]
            index = ind1.genome.index(ind2.genome[index])

        # Fill in the remaining genes from the other parent
        for i in range(num_genes):
            if child1[i] == -1:
                child1[i] = ind2.genome[i]
            if child2[i] == -1:
                child2[i] = ind1.genome[i]

        ind1.genome = child1
        ind2.genome = child2

    def __str__(self):
        return "Recombination 2 (" + f'{self.probability}' + ")"
