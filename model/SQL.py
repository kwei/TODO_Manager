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
    def __init__(self, dbName=None, tableNames=None, tableSchemas=None):
        self._db_name = dbName
        self._schemas = tableSchemas
        self._table_names = tableNames

    def get_db(self):
        if self._db_name == None:
            return None
        return sqlite3.connect(self._db_name)
    

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
        return True
    


    def get_db_name(self):
        return self._db_name
    
    def get_schemas(self):
        return self._schemas
    
    def get_table_names(self):
        return self._table_names
    

    def set_db_name(self, dbName):
        self._db_name = dbName
    
    def set_schemas(self, tableSchemas):
        self._schemas = tableSchemas
    
    def set_table_names(self, tableNames):
        self._table_names = tableNames