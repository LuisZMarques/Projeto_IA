
from abc import abstractmethod
from ga.problem import Problem
from ga.individual import Individual
from ga.genetic_algorithm import GeneticAlgorithm

class IntVectorIndividual(Individual):

    def __init__(self, problem: Problem, num_genes: int):
        super().__init__(problem, num_genes)
        self.genome = [None] * num_genes

    def initialize(self):
        for i in range(self.num_genes):
            self.genome[i] = GeneticAlgorithm.rand.randint(0, self.num_genes - 1)
            while self.genome[i] in self.genome[:i]:
                self.genome[i] = GeneticAlgorithm.rand.randint(0, self.num_genes - 1)

    def swap_genes(self, other, index: int):
        aux = self.genome[index]
        self.genome[index] = other.genome[index]
        other.genome[index] = aux

    @abstractmethod
    def compute_fitness(self) -> float:
        pass

    @abstractmethod
    def better_than(self, other: "IntVectorIndividual") -> bool:
        pass
