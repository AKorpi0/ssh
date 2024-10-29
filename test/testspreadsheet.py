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
