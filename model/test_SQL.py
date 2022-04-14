import unittest
from SQL import SQL

class TestSQL(unittest.TestCase):
    def __init__(self, *args):
        super(TestSQL, self).__init__(*args)
        self._sql = SQL()
        