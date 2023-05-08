from ga.individual_int_vector import IntVectorIndividual
import numpy as np


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        self.lenPath = 0
        self.path = []
        self.forklifts_paths = []
        # TODO

    def compute_fitness(self) -> float:
        # TODO
            self.fitness = 0

            new = np.array_split(self.genome, len(self.problem.forklifts))

            # do forklift ate ao 1º produto
            for n in range(len(self.problem.forklifts)):
                for i in self.problem.pairs:
                    if i.cell1 == self.problem.forklifts[n] and i.cell2 == self.problem.products[new[n][0]]:
                        self.fitness += i.value
                        for j in i.path:
                            self.path.append(j)
                        self.lenPath += len(i.path)

                for j in range(len(new[n]) - 1):
                    for k in self.problem.pairs:
                        if k.cell1 == self.problem.products[new[n][j + 1]] and k.cell2 == self.problem.products[new[n][j]]:
                            self.fitness += k.value
                            for l in k.path[::-1]:
                                self.path.append(l)
                            self.lenPath += len(k.path)
                        elif k.cell1 == self.problem.products[new[n][j]] and k.cell2 == self.problem.products[new[n][j + 1]]:
                            self.fitness += k.value
                            for l in k.path:
                                self.path.append(l)
                            self.lenPath += len(k.path)

                # do ultimo produto ate à exit
                for l in self.problem.pairs:
                    if l.cell1 == self.problem.products[new[n][- 1]] and l.cell2 == self.problem.exit:
                        self.fitness += l.value
                        for d in l.path:
                            self.path.append(d)
                        self.lenPath += len(l.path)

            self.forklifts_paths.append(self.path)

            return self.fitness

    def obtain_all_path(self):
        # TODOk
        print("-----")
        for i in self.forklifts_paths[0]:
            print(i)
        return [self.forklifts_paths, len(self.path)]

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
