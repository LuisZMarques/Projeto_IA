from ga.individual_int_vector import IntVectorIndividual
from warehouse.cell import Cell
from warehouse.pair import Pair


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        # TODO


    def compute_fitness(self) -> float:
        # TODO
        self.fitness = 0
        # do forklift ate ao 1º produto
        for i in self.problem.pairs:
            if i.cell1 == self.problem.forklifts[0] and i.cell2 == self.problem.products[self.genome[0]]:
                self.fitness += i.value

        for j in range(self.num_genes-1):
            for k in self.problem.pairs:
                if (k.cell1 == self.problem.products[self.genome[j]] and k.cell2 == self.problem.products[self.genome[j+1]]) or\
                        (k.cell1 == self.problem.products[self.genome[j+1]] and k.cell2 == self.problem.products[self.genome[j]]):
                    self.fitness += k.value

        # do ultimo produto ate à exit
        for l in self.problem.pairs:
            if l.cell1 == self.problem.products[self.genome[self.num_genes-1]] and l.cell2 == self.problem.exit:
                self.fitness += l.value
        return self.fitness

    def obtain_all_path(self):
        # TODO
        return [[self.problem.pairs[0]],1]

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += str (self.genome) + "\n\n"
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