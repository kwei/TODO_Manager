from dotenv import load_dotenv
import os

class Config():
    def __init__(self):
        load_dotenv()
        print("config: ", os.getenv("DB_NAME"))
        self._DB_NAME = os.getenv("DB_NAME")
    
    def db_name(self):
        return self._DB_NAME