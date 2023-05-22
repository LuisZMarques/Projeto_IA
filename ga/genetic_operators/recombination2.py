from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual import Individual
from ga.genetic_operators.recombination import Recombination

class Recombination2(Recombination):

    def __init__(self, probability: float):
        super().__init__(probability)

    def recombine(self, ind1: Individual, ind2: Individual) -> None:
        # TODO
        if GeneticAlgorithm.rand.random() < self.probability:
            cut1 = GeneticAlgorithm.rand.randint(0, ind1.num_genes-1)
            cut2 = GeneticAlgorithm.rand.randint(0, ind2.num_genes-1)

            ind1.genome = ind1.genome[:cut1] + ind2.genome[cut2:]
            ind2.genome = ind2.genome[:cut2] + ind1.genome[cut1:]


    def __str__(self):
        return "Recombination 2 (" + f'{self.probability}' + ")"
