import math

from agentsearch.heuristic import Heuristic
from warehouse.warehouse_problemforSearch import WarehouseProblemSearch
from warehouse.warehouse_state import WarehouseState


class HeuristicWarehouse(Heuristic[WarehouseProblemSearch, WarehouseState]):

    def __init__(self):
        super().__init__()

    def compute(self, state: WarehouseState) -> float:
        # TODO
        h = 0
        h = math.sqrt(
            (state.line_forklift - state.rows) ** 2 + (state.column_forklift - state.columns) ** 2)
        return 0

    def __str__(self):
        return "# TODO"

