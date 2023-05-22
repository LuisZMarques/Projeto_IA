from ga.genetic_algorithm import GeneticAlgorithm
from ga.genetic_operators.recombination import Recombination
from ga.individual import Individual

class Recombination3(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        # TODO
        while len(set(ind1.genome)) != ind1.num_genes and len(set(ind2.genome)) != ind2.num_genes:
            cut1 = GeneticAlgorithm.rand.randint(0, ind1.num_genes-1)
            cut2 = GeneticAlgorithm.rand.randint(0, ind2.num_genes-1)

            if cut1 > cut2:
                cut1, cut2 = cut2, cut1

            for i in range(cut1, cut2):
                ind1.genome[i], ind2.genome[i] = ind2.genome[i], ind1.genome[i]

    def __str__(self):
        return "Recombination 3 (" + f'{self.probability}' + ")"