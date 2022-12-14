from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId

from ...config_db import config_db


#from factory.validation import Validator
#from factory.database import Database
from ..model.todo import Database, Validator


class Todo:
    def __init__(self):
        self.validator = Validator()
        self.db = Database()

        print(self.db)

        self.collection_name = 'Clouflake'  # collection name

        self.fields = {
            "name": "string",
            "bio": "string",
            "tags": "array",
            "date": "datetime",
        }

        self.create_required_fields = ["name", "bio"]

        # Fields optional for CREATE
        self.create_optional_fields = []

        # Fields required for UPDATE
        self.update_required_fields = ["name", "bio"]

        # Fields optional for UPDATE
        self.update_optional_fields = []

    def create(self, todo):
        # Validator will throw error if invalid
        self.validator.validate(todo, self.fields, self.create_required_fields, self.create_optional_fields)
        res = self.db.insert(todo, self.collection_name)
        return "Inserted Id " + res

    def find(self, todo):  # find all
        return self.db.find(todo, self.collection_name)

    def find_by_id(self, id):
        return self.db.find_by_id(id, self.collection_name)

    def update(self, id, todo):
        self.validator.validate(todo, self.fields, self.update_required_fields, self.update_optional_fields)
        return self.db.update(id, todo,self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)

"""

#class Database(object):
def __init__(self):
    self.client = MongoClient(config_db['db']['url'])  # configure db url
    self.db = self.client[config_db['db']['name']]  # configure db name

def insert(self, element, collection_name):
    element["created"] = datetime.now()
    element["updated"] = datetime.now()
    inserted = self.db[collection_name].insert_one(element)  # insert data to db
    return str(inserted.inserted_id)

def find(self, criteria, collection_name, projection=None, sort=None, limit=0, cursor=False):  # find all from db

    if "_id" in criteria:
        criteria["_id"] = ObjectId(criteria["_id"])

    found = self.db[collection_name].find(filter=criteria, projection=projection, limit=limit, sort=sort)

    if cursor:
        return found

    found = list(found)

    for i in range(len(found)):  # to serialize object id need to convert string
        if "_id" in found[i]:
            found[i]["_id"] = str(found[i]["_id"])

    return found

def find_by_id(self, id, collection_name):
    found = self.db[collection_name].find_one({"_id": ObjectId(id)})
    
    if found is None:
        return not found
    
    if "_id" in found:
            found["_id"] = str(found["_id"])

    return found

def update(self, id, element, collection_name):
    criteria = {"_id": ObjectId(id)}

    element["updated"] = datetime.now()
    set_obj = {"$set": element}  # update value

    updated = self.db[collection_name].update_one(criteria, set_obj)
    if updated.matched_count == 1:
        return "Record Successfully Updated"

def delete(self, id, collection_name):
    deleted = self.db[collection_name].delete_one({"_id": ObjectId(id)})
    return bool(deleted.deleted_count)
"""