import numpy as np

from ga.individual_int_vector import IntVectorIndividual
from warehouse.cell import Cell
import constants
from random import shuffle

class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        self.forklifts_paths = []
        self.lenPath = 0
        # TODO

    def compute_fitness(self) -> float:
        # TODO
        self.path = [None] * len(self.problem.forklifts)
        self.fitness = 0
        self.lenPath = 0

        new = np.array_split(self.genome, len(self.problem.forklifts))

        # do forklift ate ao 1º produto
        for f in range(len(self.problem.forklifts)):
            self.path[f] = []
            for i in self.problem.pairs:
                if i.cell1 == self.problem.forklifts[f] and i.cell2 == self.problem.products[new[f][0]]:
                    self.fitness += i.value
                    for j in i.path:
                        self.path[f].append(j)

            for j in range(len(new[f])-1):
                for k in self.problem.pairs:
                    if k.cell1 == self.problem.products[new[f][j + 1]] and k.cell2 == self.problem.products[new[f][j]]:
                        self.fitness += k.value
                        for l in k.path[::-1]:
                            self.path[f].append(l)
                    elif k.cell1 == self.problem.products[new[f][j]] and k.cell2 == self.problem.products[new[f][j + 1]]:
                        self.fitness += k.value
                        for l in k.path:
                            self.path[f].append(l)

            # do ultimo produto ate à exit
            for l in self.problem.pairs:
                if l.cell1 == self.problem.products[new[f][len(new[f])-1]] and l.cell2 == self.problem.exit:
                    self.fitness += l.value
                    for d in l.path:
                        self.path[f].append(d)

            self.forklifts_paths.insert(f, self.path[f])
            if self.lenPath < len(self.path[f]):
                self.lenPath = len(self.path[f])

        return self.fitness

    def obtain_all_path(self):
        # TODOk
        return [self.forklifts_paths, self.lenPath]

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += str(self.genome) + "\n\n"
        # TODO
        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        # TODO
        return new_instance