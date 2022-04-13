import json
class DB_Controller_Task():
    def __init__(self, sql = None):
        self._sql = sql
    

    def fetchAll(self, data):
        # 1. fetch members to get the corresponding task indexes.
        # 2. according to the indexes, fetch the tasks to get the all task of the member.
        userName = data["userName"]
        if not self._sql:
            return "No sql instance."
        db = self._sql.get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * from tasks WHERE userName = ?", (userName,))
        fetchRes = cursor.fetchone()
        db.close()
        print("Tasks fetch result: ", fetchRes)
        if not fetchRes:
            return json.dumps([])
        taskList = []
        for res in fetchRes:
            taskList.append({
                "id": res[0],
                "tagSequence": res[1],
                "userName": res[2],
                "title": res[3],
                "content": res[4],
                "createTime": res[5],
                "createDate": res[6]
            })
        return json.dumps(taskList)


    def create(self, data):
        # 1. insert a new task into the tasks and return the index.
        # 2. update the indexes of the member to the members.
        userName = data["userName"]
        task = data["task"]
        if task is None:
            return "No task obj."
        tagSequence = hash(task["createTime"]+task["createDate"])
        if not self._sql:
            return "No sql instance."
        db = self._sql.get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO tasks VALUES (NULL, ?, ?, ?, ?, ?, ?)", (tagSequence, userName, task["title"], task["content"], task["createTime"], task["createDate"]))
        db.commit()
        db.close()
        return tagSequence

    
    def update(self, data):
        # 1. fetch the certain task of the member.
        # 2. update the content.
        task = data["task"]
        if task is None:
            return "No task obj."
        userName = data["userName"]
        tagSequence = data["tagSequence"]
        if not self._sql:
            return "No sql instance."
        db = self._sql.get_db()
        cursor = db.cursor()
        cursor.execute("UPDATE tasks SET title = ? content = ? createTime = ? createDate = ? WHERE userName = ? AND tagSequence = ?", (task["title"], task["content"], task["createTime"], task["createDate"], userName, tagSequence))
        db.close()
        return "Update successfully."

    
    def delete(self, data):
        # 1. fetch the certain task of the member and delete.
        # 2. according to the indexes, fetch the members to update the task of the member.
        userName = data["userName"]
        tagSequence = data["tagSequence"]
        if not self._sql:
            return "No sql instance."
        db = self._sql.get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM tasks WHERE userName = ? AND tagSequence = ?", (userName, tagSequence))
        db.close()
        return "Delete successfully."