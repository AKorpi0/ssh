from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_evaluation(self):
        ss = SpreadSheet()
        ss.set("A", "5")
        self.assertEqual(5, ss.evaluate("A"))

    def test_eval_error(self):
        ss = SpreadSheet()
        ss.set("A", "5,6")
        self.assertEqual("#Error", ss.evaluate("A"))

    def test_eval_strings(self):
        ss = SpreadSheet()
        ss.set("A", "'Apple'")
        self.assertEqual("Apple", ss.evaluate("A"))

    def test_eval_strings_error(self):
        ss = SpreadSheet()
        ss.set("A", "Apple")
        self.assertEqual("#Error", ss.evaluate("A"))

    def test_eval_formula_string(self):
        ss = SpreadSheet()
        ss.set("A", "='Apple'")
        self.assertEqual("Apple", ss.evaluate("A"))

    def test_eval_formula_num(self):
        ss = SpreadSheet()
        ss.set("A", "=1")
        self.assertEqual(1, ss.evaluate("A"))

    def test_eval_formula_error(self):
        ss = SpreadSheet()
        ss.set("A", "='Apple")
        self.assertEqual("#Error", ss.evaluate("A"))

    def test_eval_formula_error2(self):
        ss = SpreadSheet()
        ss.set("A", "=Apple'")
        self.assertEqual("#Error", ss.evaluate("A"))

    def test_eval_reference_formula(self):
        ss = SpreadSheet()
        ss.set("A", "=B1")
        ss.set("B1", "42")
        self.assertEqual(42, ss.evaluate("A"))

    def test_eval_reference_formula_error(self):
        ss = SpreadSheet()
        ss.set("A", "=B1")
        ss.set("B1", "42.5")
        self.assertEqual("#Error", ss.evaluate("A"))

