from .models import Mongo_Credentials
from pymongo import MongoClient

class mongodb():
    """
    {
    "push":'collection.update_one(query,{"$push":{f"{locator}":value }})', # Array operation only
    "pull":'collection.update_one(query,{"$pull":{f"{locator}":value }})', # Array operation only
    "unset":'collection.update_one(query,{"$unset":{f"{locator}":value }})', # Object/Dictonary operation only
    "pop":'collection.update_one(query,{"$pop":{f"{locator}":value }})',
    "set":'collection.update_one(query,{"$set":{f"{locator}":value }})',
    "set_all":'collection.update_one(query,{"$set":value})',
    "push_all":'collection.update_one(query,{"$push":value})',
    "add":'collection.insert_one(value)',
    "get":'collection.find_one(query)',
    "filter":'collection.find(query)',
    "search":'collection.find({"$text": {"$search": query}}).limit(limit_)',
    "delete":'collection.delete_one(query)'
    }
    """

    def __init__(self,use=False):
        self.use = use
        if self.use:
            self.credential = Mongo_Credentials.objects.get(use=self.use,status=True)
            self.collection = MongoClient(self.credential.uri)[self.credential.db][self.credential.collection]
        else:
            print("Credential dont exists")
        # except:
        #     self.collection = ""
        #     print("Credential Not provided")
    

    def push(self,query,**kwargs):
        kwargs = {i.replace("__","."):j for i,j in kwargs}
        self.collection.update_one(query,{"$push":kwargs})

    def pull(self,query,**kwargs):
        kwargs = {i.replace("__","."):j for i,j in kwargs}
        self.collection.update_one(query,{"$pull":kwargs})

    def unset(self,query,**kwargs):
        kwargs = {i.replace("__","."):j for i,j in kwargs}
        self.collection.update_one(query,{"$unset":kwargs})

    def pop(self,query,**kwargs):
        kwargs = {i.replace("__","."):j for i,j in kwargs}
        self.collection.update_one(query,{"$pop":kwargs})

    def set(self,query,**kwargs):
        kwargs = {i.replace("__","."):j for i,j in kwargs}
        self.collection.update_one(query,{"$set":kwargs})

    def push_all(self,query,value={},**kwargs):
        kwargs = {i.replace("__","."):j for i,j in kwargs.items() }
        value.update(kwargs)
        self.collection.update_one(query,{"$push":value})

    def set_all(self,query,value={},**kwargs):
        kwargs = {i.replace("__","."):j for i,j in kwargs.items() }
        value.update(kwargs)
        self.collection.update_one(query,{"$set":value})

    def add(self,value={},**kwargs):
        kwargs = {i.replace("__","."):j for i,j in kwargs.items() }
        if kwargs : value.update(kwargs)
        self.collection.insert_one(value)

    def delete(self,query={},**kwargs):
        kwargs = {i.replace("__","."):j for i,j in kwargs.items() }
        query.update(kwargs)
        self.collection.delete_one(query) 

    def get(self,query={},sort=[],**kwargs):
        kwargs = {i.replace("__","."):j for i,j in kwargs.items() }
        query.update(kwargs)
        return self.collection.find_one(query,sort=sort)

    def filter(self,query={},sort=[],**kwargs):
        kwargs = {i.replace("__","."):j for i,j in kwargs.items() }
        query.update(kwargs)
        return self.collection.find(query,sort=sort)

    def search(self,query,limit=10):
        return self.collection.find({"$text": {"$search": query}}).limit(limit)
    
    def search_index(self, search_index = []):
        """
        e.g. : search_index = [("name","text"),("description","text")]
        """
        self.collection.create_index(search_index)