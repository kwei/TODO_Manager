import unittest
from unittest import mock
from config import Config

class Test_Config(unittest.TestCase):
    def setUp(self):
        pass
    
    @mock.patch('os.getenv')
    def test_db_name(self, mock_getenv_func):
        mock_getenv_func.return_value = "test"
        config = Config()
        self.assertEqual(config.db_name(), "test")


if __name__ == "__main__":
    unittest.main()