import unittest
from unittest import mock
from unittest.mock import MagicMock, create_autospec
from SQL import SQL
import sqlite3
class TestSQL(unittest.TestCase):
    @mock.patch("sqlite3.connect")
    def setUp(self, mock_sqlite3_connect_func):
        self._test_db_name = ":memory:"
        self._test_db_table_name = ["test"]
        self._test_scheme = {
            "test": "CREATE TABLE test (\
                    id INTEGER PRIMARY KEY AUTOINCREMENT,\
                    tagSequence varchar(255) NOT NULL,\
                    userName varchar(255) NOT NULL,\
                    title varchar(255) NOT NULL,\
                    content varchar(255) NOT NULL,\
                    createTime time NOT NULL,\
                    createDate date NOT NULL);"
        }
        self._sql = create_autospec(SQL)
        self._sql.get_db.return_value = mock_sqlite3_connect_func.return_value
        self._conn = self._sql.get_db.return_value
        self._conn.cursor = MagicMock()
        self._cursor = self._conn.cursor.return_value
        self._cursor.execute = MagicMock()
        self._cursor.commit = MagicMock()
    

    def test_get_db(self):
        self._conn.return_value = True
        sql = SQL(self._test_db_name, self._test_db_table_name, self._test_scheme)
        self.assertTrue(sql.get_db())
    

    def test_init_db(self):
        sql = SQL(self._test_db_name, self._test_db_table_name, self._test_scheme)
        self._cursor.fetchone = MagicMock()
        self._cursor.fetchone.return_value = True
        self._conn.executescript = MagicMock()
        self._cursor.executescript.return_value = True
        self.assertTrue(sql.init_db())
        

if __name__ == "__main__":
    unittest.main()