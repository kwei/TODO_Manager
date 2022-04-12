
class DB_Controller_Task():
    def __init__(self, sql = None):
        self._sql = sql
    

    def fetchAll(self, data):
        # 1. fetch members to get the corresponding task indexes.
        # 2. according to the indexes, fetch the tasks to get the all task of the member.
        pass


    def create(self, data):
        # 1. insert a new task into the tasks and return the index.
        # 2. update the indexes of the member to the members.
        pass

    
    def update(self, data):
        # 1. fetch the certain task of the member.
        # 2. update the content.
        pass

    
    def delete(self, data):
        # 1. fetch the certain task of the member and delete.
        # 2. according to the indexes, fetch the members to update the task of the member.
        pass