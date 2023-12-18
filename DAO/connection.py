from UTIL.connection import DBConnection

class PropertyUtil:
    def __init__(self):
        PropertyUtil.connection=DBConnection.getConnection()
obj=PropertyUtil()