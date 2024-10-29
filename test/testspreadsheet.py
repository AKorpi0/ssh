from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_evaluation(self):
        ss = SpreadSheet()
        ss.set("A", "5")
        self.assertEqual(5, ss.evaluate("A"))
