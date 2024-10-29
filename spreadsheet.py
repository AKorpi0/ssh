
class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._evaluating = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> int | str | float:
        if cell in self._evaluating:
            return "#Circular"
        self._evaluating.add(cell)
        value = self._cells[cell]
        if value.startswith("='") and value.endswith("'"):
            result = value[2:-1]
        elif value.startswith("'") and value.endswith("'"):
            result = value[1:-1]
        elif value.startswith("="):
            expr = value[1:]
            if expr.isdigit():
                result = int(expr)
            elif expr.isidentifier() and expr in self._cells:
                result = self.evaluate(expr)
            else:
                try:
                    # Evaluate the expression safely
                    result = eval(expr, {"__builtins__": None}, {k: self.evaluate(k) for k in self._cells})
                    if isinstance(result, int):
                        result = int(result)  # Allow float results directly
                    else:
                        result = "#Error"
                except:
                    result = "#Error"
        else:
            try:
                result = int(value)
            except ValueError:
                result = "#Error"
        self._evaluating.remove(cell)
        return result

