import numpy as np

from ga.individual_int_vector import IntVectorIndividual
import random

class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        self.forklifts_paths = []
        self.best_forklifts_paths = []
        self.lenPath = 0

    def compute_fitness(self) -> float:
        # TODO
        self.path = [None] * len(self.problem.forklifts)
        self.fitness = 0
        self.penalizacao = 0
        forklifts_paths = []
        # Definir o número de pontos de divisão
        num_pontos_divisao = len(self.problem.forklifts)-1

        # Gerar pontos de divisão aleatórios
        pontos_divisao = random.sample(range(1, len(self.genome)), num_pontos_divisao)

        # Ordenar os pontos de divisão
        pontos_divisao.sort()

        # Dividir o array em partes desiguais com os pontos de divisão aleatórios
        new = np.split(self.genome, pontos_divisao)

        for f in range(len(self.problem.forklifts)):
            # do forklift ate ao 1º produto
            for i in self.problem.pairs:
                if i.cell1 == self.problem.forklifts[f] and i.cell2 == self.problem.products[new[f][0]]:
                    self.fitness += i.value
                    forklifts_paths.append(i.path)
            for j in range(len(new[f]) - 1):
                for k in self.problem.pairs:
                    if k.cell1 == self.problem.products[new[f][j + 1]] and k.cell2 == self.problem.products[new[f][j]]:
                        self.fitness += k.value
                        forklifts_paths.append(k.path[::-1])
                    elif k.cell1 == self.problem.products[new[f][j]] and k.cell2 == self.problem.products[
                        new[f][j + 1]]:
                        self.fitness += k.value
                        forklifts_paths.append(k.path)

            # do ultimo produto ate à exit
            for l in self.problem.pairs:
                if l.cell1 == self.problem.products[new[f][len(new[f]) - 1]] and l.cell2 == self.problem.exit:
                    self.fitness += l.value
                    forklifts_paths.append(l.path)

            # calcular a penalização
            zipped_paths = list(zip(*forklifts_paths))

            for paths in zipped_paths:
                if len(set(paths)) < len(paths):
                    self.penalizacao += 1

            #print(self.penalizacao)


            self.best_forklifts_paths = new

        return self.fitness+self.penalizacao

    def obtain_all_path(self):
        # TODO
        self.path = [None] * len(self.problem.forklifts)
        self.lenPath = 0

        # do forklift ate ao 1º produto
        for f in range(len(self.best_forklifts_paths)):
            self.path[f] = []

            for i in self.problem.pairs:
                if i.cell1 == self.problem.forklifts[f] and i.cell2 == self.problem.products[self.best_forklifts_paths[f][0]]:
                    for j in i.path:
                        self.path[f].append(j)
            # do 1º produto ate ao 2º produto
            for j in range(len(self.best_forklifts_paths[f]) - 1):
                for k in self.problem.pairs:
                    if k.cell1 == self.problem.products[self.best_forklifts_paths[f][j + 1]] and k.cell2 == self.problem.products[self.best_forklifts_paths[f][j]]:
                        for l in k.path[::-1]:
                            self.path[f].append(l)
                    elif k.cell1 == self.problem.products[self.best_forklifts_paths[f][j]] and k.cell2 == self.problem.products[self.best_forklifts_paths[f][j + 1]]:
                        for l in k.path:
                            self.path[f].append(l)

            # do ultimo produto ate à exit
            for l in self.problem.pairs:
                if l.cell1 == self.problem.products[self.best_forklifts_paths[f][len(self.best_forklifts_paths[f]) - 1]] and l.cell2 == self.problem.exit:
                    for j in l.path:
                        self.path[f].append(j)

            self.forklifts_paths.insert(f, self.path[f])

            if self.lenPath < len(self.path[f]):
                self.lenPath = len(self.path[f])

        return [self.forklifts_paths, self.lenPath]

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += 'Genoma: '+str(self.genome) + "\n\n"
        string += 'Penalização:' + str(self.penalizacao) + "\n\n"
        # imprimir o caminho de cada empilhador
        for i in range(len(self.best_forklifts_paths)):
            string += 'Forklift ' + str(i) + ' Path: ' + str(self.best_forklifts_paths[i]) + "\n\n"

        # TODO
        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        new_instance.penalizacao = self.penalizacao
        new_instance.best_forklifts_paths = self.best_forklifts_paths.copy()
        # TODO
        return new_instance

    def compare_arrays(*arrays):
        penalizacao = 0

        # Encontra o tamanho máximo entre os arrays
        max_length = max(len(arr) for arr in arrays)

        for i in range(max_length):
            elements = [arr[i] for arr in arrays if i < len(arr)]
            if len(set(elements)) < len(elements):
                penalizacao += 1

        return penalizacao