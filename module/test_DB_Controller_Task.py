import unittest
import sys
import json
from unittest import mock
from unittest.mock import MagicMock, create_autospec
from DB_Controller_Task import DB_Controller_Task
sys.path.append('../')
from model.SQL import SQL

class Test_DB_Controller_Task(unittest.TestCase):
    @mock.patch("sqlite3.connect")
    def setUp(self, mock_sqlite3_connect_func):
        self._sql = create_autospec(SQL)
        self._sql.get_db.return_value = mock_sqlite3_connect_func.return_value
        self._conn = self._sql.get_db.return_value
        self._conn.cursor = MagicMock()
        self._cursor = self._conn.cursor.return_value
        self._cursor.execute = MagicMock()
        self._cursor.commit = MagicMock()
    
    def test_fetchAll(self):
        self._cursor.fetchall = MagicMock()
        self._cursor.fetchall.return_value = [(
            "id",
            "tagSequence",
            "userName",
            "title",
            "content",
            "createTime",
            "createDate"
        )]

        db_controller_task = DB_Controller_Task(self._sql)
        self.assertEqual(db_controller_task.fetchAll({"userName": "userName"}), json.dumps([{
            "id": "id",
            "tagSequence": "tagSequence",
            "userName": "userName",
            "title": "title",
            "content": "content",
            "createTime": "createTime",
            "createDate": "createDate"
        }]))
    
    def test_create(self):
        db_controller_task = DB_Controller_Task(self._sql)
        self.assertEqual(db_controller_task.create({
            "userName": "userName",
            "task": {
                "id": "id",
                "tagSequence": None,
                "userName": "userName",
                "title": "title",
                "content": "content",
                "createTime": "createTime",
                "createDate": "createDate"
            }}),
            json.dumps({
                "id": "id",
                "tagSequence": hash("createTime"+"createDate"),
                "userName": "userName",
                "title": "title",
                "content": "content",
                "createTime": "createTime",
                "createDate": "createDate"
            }))
    
    def test_update(self):
        db_controller_task = DB_Controller_Task(self._sql)
        self.assertEqual(db_controller_task.update({
            "userName": "userName",
            "task": {
                "id": "id",
                "tagSequence": None,
                "userName": "userName",
                "title": "title",
                "content": "content",
                "createTime": "createTime",
                "createDate": "createDate"
            },
            "tagSequence": hash("createTime"+"createDate")}), "Update successfully.")

    def test_delete(self):
        db_controller_task = DB_Controller_Task(self._sql)
        self.assertEqual(db_controller_task.delete({
            "userName": "userName",
            "tagSequence": hash("createTime"+"createDate")}), "Delete successfully.")
        

if __name__ == "__main__":
    unittest.main()