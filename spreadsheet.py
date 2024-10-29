
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
        if value.startswith("'") and value.endswith("'"):
            return value.strip("'")
        try:
            num = int(value)
            return num
        except ValueError:
            return "#Error"

