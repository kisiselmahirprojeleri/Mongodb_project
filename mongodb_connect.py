from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self,url='mongodb+srv://unityuby:mahir@cluster0.jelt3.mongodb.net/'):
        self.client = MongoClient(url)

    
    def database_getir(self, db_name):
        return self.client[db_name]