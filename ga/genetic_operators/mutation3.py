import random

from ga.genetic_algorithm import GeneticAlgorithm
from ga.individual_int_vector import IntVectorIndividual
from ga.genetic_operators.mutation import Mutation

class Mutation3(Mutation):
    def __init__(self, probability):
        super().__init__(probability)

    def mutate(self, ind: IntVectorIndividual) -> None:
        # TODO
        if GeneticAlgorithm.rand.random() < self.probability:
            random.shuffle(ind.genome)

            while len(set(ind.genome)) != len(ind.genome):
                self.mutacao(ind.genome)

    def mutacao(self, genoma):
        i = random.randint(0, len(genoma) - 1)
        j = random.randint(0, len(genoma) - 1)
        genoma[i], genoma[j] = genoma[j], genoma[i]

    def __str__(self):
        return "Mutation 3 (" + f'{self.probability}' + ")"
