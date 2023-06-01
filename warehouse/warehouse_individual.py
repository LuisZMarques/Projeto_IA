import numpy as np

from ga.individual_int_vector import IntVectorIndividual
from warehouse.cell import Cell
import constants, random
from random import shuffle


class WarehouseIndividual(IntVectorIndividual):

    def __init__(self, problem: "WarehouseProblem", num_genes: int):
        super().__init__(problem, num_genes)
        #self.biggest_path_steps = 0
        self.gen_divided = []
        

    def compute_fitness(self) -> float:
        self.fitness = 0
        self.penalizacao = 0

        forklifts_paths, big_path_steps = self.obtain_all_path()

        for p in forklifts_paths:
            self.fitness += len(p)

        # cria listas com as celulas de cada path a cada step (zip.py)
        zipped_paths = list(zip(*forklifts_paths))

        for paths in zipped_paths:
            #Teve que se implementado __hash__ na classe Cell para que o set funcionasse
            if len(set(paths)) < len(paths):
                self.penalizacao += 1

        print("Penalização: ", self.penalizacao)

        self.fitness = self.fitness + self.penalizacao

        return self.fitness

    def obtain_all_path(self):
        self.forklifts_paths = []
        self.path = [None] * len(self.problem.forklifts)
        self.biggest_path_steps = 0

        num_pontos_divisao = len(self.problem.forklifts)-1

        # Gerar pontos de divisão aleatórios
        pontos_divisao = random.sample(range(1, len(self.genome)), num_pontos_divisao)

        # Ordenar os pontos de divisão
        pontos_divisao.sort()

        # Dividir o array em partes desiguais com os pontos de divisão aleatórios
        new = np.split(self.genome, pontos_divisao)

        # do forklift ate ao 1º produto
        for f in range(len(self.problem.forklifts)):
            self.path[f] = []
            for i in self.problem.pairs:
                if i.cell1 == self.problem.forklifts[f] and i.cell2 == self.problem.products[new[f][0]]:
                    for j in i.path:
                        self.path[f].append(j)
            for j in range(len(new[f]) - 1):
                for k in self.problem.pairs:
                    if k.cell1 == self.problem.products[new[f][j + 1]] and k.cell2 == self.problem.products[new[f][j]]:
                        for l in k.path[::-1]:
                            self.path[f].append(l)
                    elif k.cell1 == self.problem.products[new[f][j]] and k.cell2 == self.problem.products[
                        new[f][j + 1]]:
                        for l in k.path:
                            self.path[f].append(l)

            # do ultimo produto ate à exit
            for l in self.problem.pairs:
                if l.cell1 == self.problem.products[new[f][len(new[f]) - 1]] and l.cell2 == self.problem.exit:
                    for d in l.path:
                        self.path[f].append(d)

            self.forklifts_paths.insert(f, self.path[f])
            if self.biggest_path_steps < len(self.path[f]):
                self.biggest_path_steps = len(self.path[f])

        self.gen_divided = new

        return [self.forklifts_paths, self.biggest_path_steps]

    def __str__(self):
        string = 'Fitness: ' + f'{self.fitness}' + '\n'
        string += 'Genoma: ' + str(self.genome) + "\n"
        string += 'Colisões Totais: ' + f'{self.penalizacao}' + "\n\n"
        for i in range(len(self.gen_divided)):
            string += 'Forklift ' + str(i) + ': ' + str(self.gen_divided[i]) + "\n"
        return string

    def better_than(self, other: "WarehouseIndividual") -> bool:
        return True if self.fitness < other.fitness else False

    # __deepcopy__ is implemented here so that all individuals share the same problem instance
    def __deepcopy__(self, memo):
        new_instance = self.__class__(self.problem, self.num_genes)
        new_instance.genome = self.genome.copy()
        new_instance.fitness = self.fitness
        new_instance.penalizacao = self.penalizacao
        for i in range(len(self.gen_divided)):
            new_instance.gen_divided.insert(i, self.gen_divided[i].copy())
        # TODO
        return new_instance