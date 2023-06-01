class Cell:
    def __init__(self, line: int, column: int):
        self.line = line
        self.column = column

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Cell):
            return False
        return self.line == other.line and self.column == other.column

    def __str__(self) -> str:
        return f"{self.line}-{self.column}"
    
    #define a hash number for the cell
    def __hash__(self) -> int:
        return hash((self.line, self.column))