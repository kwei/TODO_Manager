from config import Config
import sqlite3
import sys

'''
db_name = "database.db"
table_names = ["member", "task"]
schemas = {
    "member": schema_member.sql, 
    "task": schema_sql.sql
    }
'''

class SQL():
    def __init__(self, db_name=None, table_names=None, schemas=None):
        self._db_name = db_name
        self._schemas = schemas
        self._table_names = table_names

    def get_db(self):
        if self._db_name() == None:
            return None
        return sqlite3.connect(self._db_name())
    

    def init_db(self):
        db = self.get_db()
        cursor = db.cursor()
        for table_name in self._table_names:
            cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='" + table_name +"'")
            if not cursor.fetchone()[0]:
                print("Table {} is not existed.".format(table_name), file=sys.stdout)
                db.executescript(self._schemas[table_name])
                db.commit()
            else:
                print("Table {} is existed.".format(table_name), file=sys.stdout)
        db.close()
    


    @property
    def db_name(self):
        return self._db_name
    
    @property
    def schemas(self):
        return self._schemas
    
    @property
    def table_names(self):
        return self._table_names
    

    @db_name.setter
    def db_name(self, db_name):
        self._db_name = db_name
    
    @schemas.setter
    def schemas(self, schemas):
        self._schemas = schemas
    
    @table_names.setter
    def table_names(self, table_names):
        self._table_names = table_names