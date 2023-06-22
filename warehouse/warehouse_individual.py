import numpy as np

from ga.individual_int_vector import IntVectorIndividual
import random


class WarehouseIndividual(IntVectorIndividual):
    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        self.path = None
        self.forklifts_paths = []
        self.best_forklifts_paths = []
        self.lenPath = 0

    def compute_fitness(self) -> float:
        self.fitness = 0
        self.penalizacao = 0
        forklifts_paths = []
        num_pontos_divisao = len(self.problem.forklifts) - 1
        pontos_divisao = random.sample(range(1, len(self.genome)), num_pontos_divisao)
        pontos_divisao.sort()
        new = [np.split(self.genome, pontos_divisao)[f] for f in range(len(self.problem.forklifts))]

        for f, forklift in enumerate(self.problem.forklifts):
            forklifts_paths.append([])
            for i in self.problem.pairs:
                if i.cell1 == forklift and i.cell2 == self.problem.products[new[f][0]]:
                    self.fitness += i.value
                    forklifts_paths[f].append(i.path)

            for j in range(len(new[f]) - 1):
                for k in self.problem.pairs:
                    if k.cell1 == self.problem.products[new[f][j + 1]] and k.cell2 == self.problem.products[new[f][j]]:
                        self.fitness += k.value
                        forklifts_paths[f].append(k.path[::-1])
                    elif k.cell1 == self.problem.products[new[f][j]] and k.cell2 == self.problem.products[
                        new[f][j + 1]]:
                        self.fitness += k.value
                        forklifts_paths[f].append(k.path)

            for l in self.problem.pairs:
                if l.cell1 == self.problem.products[new[f][-1]] and l.cell2 == self.problem.exit:
                    self.fitness += l.value
                    forklifts_paths[f].append(l.path)

            # zipped_paths = list(zip(*forklifts_paths))

            # if any(len(set(paths)) < len(paths) for paths in zipped_paths):
                # self.penalizacao += 1

        self.penalizacao= self.verificar_cruzamento_entre_forklifts(forklifts_paths)

        self.best_forklifts_paths = new

        return self.fitness + self.penalizacao

    def sao_celulas_adjacentes(self, celula1, celula2):
        if abs(celula1.line - celula2.line) + abs(celula1.column - celula2.column) == 1:
            return 1
        else:
            return 0

    def verificar_cruzamento_entre_forklifts(self, array):
        penalizacao = 0
        # comparar elementos da array na mesma posição
        for i in range(len(array)-1):
            for j in range(len(array[i])-1):
                for k in range(len(array)):
                    for l in range(len(array[k])):
                        if i != k and j != l:
                            penalizacao += self.sao_celulas_adjacentes(array[i][j][0], array[k][l][0])
        return penalizacao

    def obtain_all_path(self):
        self.path = [[] for _ in range(len(self.problem.forklifts))]
        self.lenPath = 0

        for f, forklift in enumerate(self.best_forklifts_paths):
            for i in self.problem.pairs:
                if i.cell1 == self.problem.forklifts[f] and i.cell2 == self.problem.products[forklift[0]]:
                    self.path[f].extend(i.path)

            for j in range(len(forklift) - 1):
                for k in self.problem.pairs:
                    if k.cell1 == self.problem.products[forklift[j + 1]] and k.cell2 == self.problem.products[
                        forklift[j]]:
                        self.path[f].extend(k.path[::-1])
                    elif k.cell1 == self.problem.products[forklift[j]] and k.cell2 == self.problem.products[
                        forklift[j + 1]]:
                        self.path[f].extend(k.path)

            for l in self.problem.pairs:
                if l.cell1 == self.problem.products[forklift[-1]] and l.cell2 == self.problem.exit:
                    self.path[f].extend(l.path)

            self.forklifts_paths.insert(f, self.path[f])

            if self.lenPath < len(self.path[f]):
                self.lenPath = len(self.path[f])

        return [self.forklifts_paths, self.lenPath]

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += 'Genoma: ' + str(self.genome) + "\n\n"
        string += 'Penalização:' + str(self.penalizacao) + "\n\n"

        for i, paths in enumerate(self.best_forklifts_paths):
            string += 'Forklift ' + str(i) + ' Path: ' + str(paths) + "\n\n"

        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return self.fitness < other.fitness

    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        new_instance.penalizacao = self.penalizacao
        new_instance.best_forklifts_paths = self.best_forklifts_paths.copy()
        return new_instance
