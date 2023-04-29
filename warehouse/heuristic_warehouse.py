import math

from agentsearch.heuristic import Heuristic
from warehouse.warehouse_problemforSearch import WarehouseProblemSearch
from warehouse.warehouse_state import WarehouseState


class HeuristicWarehouse(Heuristic[WarehouseProblemSearch, WarehouseState]):

    def __init__(self):
        super().__init__()

    def compute(self, state: WarehouseState) -> float:
        # Calcula a distância em linha reta da forklift até a posição final
        distance = math.sqrt(
            (state.forklift_row - state.final_row) ** 2 + (state.forklift_column - state.final_column) ** 2)
        return distance


    def __str__(self):
       return "forklift distance to final position"

