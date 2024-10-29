
class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._evaluating = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> int | str:
        value = self._cells[cell]
        if value.startswith("='") and value.endswith("'"):
            return value[2:-1]
        elif value.startswith("'") and value.endswith("'"):
            return value[1:-1]
        elif value.startswith("="):
            try:
                return int(value[1:])
            except ValueError:
                return value[1:]
        try:
            return int(value)
        except ValueError:
            return "#Error"

