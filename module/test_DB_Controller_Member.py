import unittest
import sys
from unittest import mock
from unittest.mock import MagicMock, create_autospec
from DB_Controller_Member import DB_Controller_Member
sys.path.append('../')
from model.SQL import SQL

class Test_DB_Controller_Member(unittest.TestCase):
    @mock.patch("sqlite3.connect")
    def setUp(self, mock_sqlite3_connect_func):
        self._sql = create_autospec(SQL)
        self._sql.get_db.return_value = mock_sqlite3_connect_func.return_value
        self._conn = self._sql.get_db.return_value
        self._conn.cursor = MagicMock()
        self._cursor = self._conn.cursor.return_value
        self._cursor.execute = MagicMock()
        self._cursor.commit = MagicMock()
    
    def test_isExist(self, ):
        self._cursor.fetchone = MagicMock()
        self._cursor.fetchone.return_value = True

        db_controller_member = DB_Controller_Member(self._sql)
        self.assertTrue(db_controller_member.isExist())

        self._cursor.fetchone.return_value = False

        db_controller_member = DB_Controller_Member(self._sql)
        self.assertFalse(db_controller_member.isExist())
    
    def test_fetch(self):
        self._cursor.fetchone = MagicMock()
        self._cursor.fetchone.return_value = (
            "id",
            "userName",
            "userPassword"
        )

        db_controller_member = DB_Controller_Member(self._sql)
        self.assertEqual(db_controller_member.fetch(), {
            "id": "id",
            "userName": "userName",
            "userPassword": "userPassword"
        })
    
    def test_insert(self):
        self._cursor.fetchone = MagicMock()
        self._cursor.fetchone.return_value = (
            "id",
            "userName"
        )

        db_controller_member = DB_Controller_Member(self._sql)
        self.assertEqual(db_controller_member.insert(), (
            "id",
            "userName"
        ))
        

if __name__ == "__main__":
    unittest.main()