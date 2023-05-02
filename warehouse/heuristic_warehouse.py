import math

import numpy as np

from agentsearch.heuristic import Heuristic
from warehouse.warehouse_problemforSearch import WarehouseProblemSearch
from warehouse.warehouse_state import WarehouseState


class HeuristicWarehouse(Heuristic[WarehouseProblemSearch, WarehouseState]):

    def __init__(self):
        super().__init__()
        self._lines_goal_matrix=None
        self._cols_goal_matrix=None
    def compute(self, state: WarehouseState) -> float:
        # TODO
        h = 0
        h = abs(state.line_forklift-self._problem.goal_position.line) + abs(state.column_forklift-self._problem.goal_position.column)
        return h

    def __str__(self):
        return "# TODO"
