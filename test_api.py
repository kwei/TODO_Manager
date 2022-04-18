import unittest
from unittest import mock
from unittest.mock import MagicMock
import requests
import json


class Test_Api(unittest.TestCase):
    def setUp(self):
        self._userName = "KW"
        self._pass = "123"

        self._root = "http://127.0.0.1:5000"

        self._homePage = self._root + "/home"
        self._login = self._root + "/login"
        self._logout = self._root + "/logout"
        self._register = self._root + "/register"

        self._taskFetchAll = self._root + "/tasks/fetchAll/"
        self._taskCreate = self._root + "/tasks/create/"
        self._taskUpdate = self._root + "/tasks/update/"
        self._taskDelete = self._root + "/tasks/delete/"
    

    def test_homePage(self):
        res = requests.get(self._homePage)
        self.assertEqual(res.status_code, 200)


    def test_login(self):
        res = requests.get(self._login)
        self.assertEqual(res.status_code, 200)

        res = requests.post(self._login, data = {
            "userName": self._userName,
            "password": self._pass
        })
        self.assertEqual(res.status_code, 200)
    

    def test_logout(self):
        res = requests.get(self._logout)
        self.assertEqual(res.status_code, 200)

    @mock.patch('module.DB_Controller_Member.DB_Controller_Member')
    def test_register(self, mock_DB_Controller_Member):
        res = requests.post(self._register, data = {
            "userName": self._userName,
            "password": self._pass,
            "password-check": self._pass
        })
        mock_DB_Controller_Member.isExist = MagicMock()
        mock_DB_Controller_Member.isExist.return_value = True
        self.assertEqual(res.status_code, 200)

        mock_DB_Controller_Member.isExist.return_value = False
        mock_DB_Controller_Member.insert = MagicMock()
        mock_DB_Controller_Member.insert.return_value = ("id", "userName")
        self.assertEqual(res.status_code, 200)

    @mock.patch('module.DB_Controller_Task.DB_Controller_Task')
    def test_taskFetchAll(self, mock_DB_Controller_Task):
        mock_DB_Controller_Task.fetchAll = MagicMock()
        mock_DB_Controller_Task.fetchAll.return_value = json.dumps([{
            "id": "id",
            "tagSequence": "tagSequence",
            "userName": "userName",
            "title": "title",
            "content": "content",
            "createTime": "createTime",
            "createDate": "createDate"
        }])
        res = requests.get(self._taskFetchAll + self._userName)
        self.assertEqual(res.status_code, 200)

    @mock.patch('module.DB_Controller_Task.DB_Controller_Task')
    def test_taskCreate(self, mock_DB_Controller_Task):
        mock_DB_Controller_Task.create = MagicMock()
        mock_DB_Controller_Task.create.return_value = json.dumps([{
            "id": "id",
            "tagSequence": "tagSequence",
            "userName": "userName",
            "title": "title",
            "content": "content",
            "createTime": "createTime",
            "createDate": "createDate"
        }])
        res = requests.post(self._taskCreate + self._userName)
        self.assertEqual(res.status_code, 200)

    @mock.patch('module.DB_Controller_Task.DB_Controller_Task')
    def test_taskUpdate(self, mock_DB_Controller_Task):
        mock_DB_Controller_Task.update = MagicMock()
        mock_DB_Controller_Task.update.return_value = "Update successfully."
        res = requests.post(self._taskUpdate + self._userName + "/tagSequence")
        self.assertEqual(res.status_code, 200)

    @mock.patch('module.DB_Controller_Task.DB_Controller_Task')
    def test_taskDelete(self, mock_DB_Controller_Task):
        mock_DB_Controller_Task.delete = MagicMock()
        mock_DB_Controller_Task.delete.return_value = "Delete successfully."
        res = requests.get(self._taskDelete + self._userName + "/tagSequence")
        self.assertEqual(res.status_code, 200)





if __name__ == "__main__":
    unittest.main()