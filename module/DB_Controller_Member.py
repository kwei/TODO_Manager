
class DB_Controller_Member():
    def __init__(self, sql = None):
        self._sql = sql
    
    def isExist(self, userName = ""):
        if not self._sql:
            return None
        db = self._sql.get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * from members WHERE userName = ?", (userName,))
        if not cursor.fetchone():
            db.close()
            return False
        else:
            db.close()
            return True
    
    def fetch(self, userName = "", userPassword = ""):
        if not self._sql:
            return None
        db = self._sql.get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * from members WHERE userName = ? and userPassword = ?", (userName, userPassword))
        data = cursor.fetchone()
        account = {
            "id": data[0],
            "userName": data[1],
            "userPassword": data[2]
        }
        db.close()
        return account
    
    def insert(self, userName = "", userPassword = ""):
        if not self._sql:
            return None
        db = self._sql.get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO members VALUES (NULL, ?, ?)", (userName, userPassword))
        db.commit()
        cursor.execute("SELECT * from members WHERE userName = ? and userPassword = ?", (userName, userPassword))
        data = cursor.fetchone()
        db.close()
        return data[0], data[1]
