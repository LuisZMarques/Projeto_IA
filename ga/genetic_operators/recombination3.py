from ga.genetic_algorithm import GeneticAlgorithm
from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual

class Recombination3(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)
    #Recombination Cycle Crossover (CX):
    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        num_genes = ind1.num_genes
        cut1 = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        cut2 = GeneticAlgorithm.rand.randint(0, num_genes - 1)
        if cut2 < cut1:
            cut1, cut2 = cut2, cut1

        # Create the first child by copying the selected segment from ind1
        # and filling in the remaining genes from ind2
        child1 = [-1] * len(ind1.genome)
        child1[cut1:cut2 + 1] = ind1.genome[cut1:cut2 + 1]
        remaining_genes = [gene for gene in ind2.genome if gene not in child1[cut1:cut2 + 1]]
        child1[:cut1] = remaining_genes[:cut1]
        child1[cut2 + 1:] = remaining_genes[cut1:]

        # Create the second child by copying the selected segment from ind2
        # and filling in the remaining genes from ind1
        child2 = [-1] * len(ind1.genome)
        child2[cut1:cut2 + 1] = ind2.genome[cut1:cut2 + 1]
        remaining_genes = [gene for gene in ind1.genome if gene not in child2[cut1:cut2 + 1]]
        child2[:cut1] = remaining_genes[:cut1]
        child2[cut2 + 1:] = remaining_genes[cut1:]

        ind1.genome = child2
        ind2.genome = child1ind1.genome[i], ind2.genome[i] = ind2.genome[i], ind1.genome[i]

    def __str__(self):
        return "Recombination 3 (" + f'{self.probability}' + ")"