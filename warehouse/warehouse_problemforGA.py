from ga.problem import Problem
from warehouse.warehouse_agent_search import WarehouseAgentSearch
from warehouse.warehouse_individual import WarehouseIndividual

class WarehouseProblemGA(Problem):

    def __init__(self, agent_search: WarehouseAgentSearch):
        # TODO
        self.forklifts = agent_search.forklifts
        self.products = agent_search.products
        self.agent_search = agent_search
        self.pairs = agent_search.pairs
        self.exit = agent_search.exit
        self.count = 0

    def generate_individual(self) -> "WarehouseIndividual":
        # TODO
        new_individual = WarehouseIndividual(self, len(self.products))
        new_individual.initialize()
        return new_individual

    def __str__(self):
        string = "# of forklifts: "
        string += f'{len(self.forklifts)}'
        string = "# of products: "
        string += f'{len(self.products)}'
        return string

