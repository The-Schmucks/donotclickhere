from pymongo import MongoClient

class Database(object):
    URI = "mongodb+srv://munezaclovis:YdSR48Dzd3YOBfEo@machinelearning.y2c2l.azure.mongodb.net/machinelearning?retryWrites=true&w=majority"
    DBNAME = None

    @staticmethod
    def initialize():
        client = MongoClient(Database.URI)
        Database.DBNAME = client['MachineLearning']

    @staticmethod
    def __init__():
        Database.initialize()

    @staticmethod
    def insert(collection, data):
        Database.DBNAME[collection].insert(data)

    @staticmethod
    def find(collection, query=None):
        return Database.to_dict(Database.DBNAME[collection].find(query))

    @staticmethod
    def findAll(collection):
        return Database.to_dict(Database.DBNAME[collection].find())

    @staticmethod
    def find_one(collection, query=None):
        return Database.to_dict(Database.DBNAME[collection].find_one(query))

    @staticmethod
    def update(collection, query, data):
        Database.DBNAME[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query=None):
        return Database.DBNAME[collection].remove(query)

    @staticmethod
    def to_dict(cursorData):
        dictionary = {}
        for item in cursorData:
            dictionary[item['_id']] = item
        return dictionary
