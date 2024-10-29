
class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._evaluating = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> int | str:
        if cell in self._evaluating:
            return "#Error"
        self._evaluating.add(cell)
        
        value = self.get(cell)
        if value.startswith("='") and value.endswith("'"):
            result = value[2:-1]
        elif value.startswith("'") and value.endswith("'"):
            result = value[1:-1]
        elif value.startswith("="):
            if value[1:].isnumeric():
                result = int(value[1:])
            else:
                # Check if it's a valid cell reference
                ref_value = self.evaluate(value[1:])
                if isinstance(ref_value, int):
                    result = ref_value
                else:
                    result = "#Error"
        else:
            try:
                result = int(value)
            except ValueError:
                result = "#Error"
        
        self._evaluating.remove(cell)
        return result

