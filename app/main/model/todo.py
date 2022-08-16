from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId

from ...config_db import config_db


class Database(object):
    def __init__(self):
        print(config_db['db']['url'])
        self.client = MongoClient(config_db['db']['url'])  # configure db url
        self.db = self.client[config_db['db']['name']]  # configure db name

        print(self.client)
        print(self.db)

    def insert(self, element, collection_name):
        element["date"] = datetime.now()
        #element["updated"] = datetime.now()
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

        element["date"] = datetime.now()
        set_obj = {"$set": element}  # update value

        updated = self.db[collection_name].update_one(criteria, set_obj)
        if updated.matched_count == 1:
            return "Record Successfully Updated"

    def delete(self, id, collection_name):
        deleted = self.db[collection_name].delete_one({"_id": ObjectId(id)})
        return bool(deleted.deleted_count)

class Validator(object):
    def validate_type(self, element, desired_type):
        if desired_type == "int":
            return type(element) == int
        if desired_type == "string":
            return type(element) == str
        if desired_type == "datetime":
            return isinstance(element, datetime)
        if desired_type == "float":
            return type(element) == float
        if type(desired_type) == list:
            return (element in desired_type)
        raise ValueError("Invalid value for desired type")

    def validateTypes(self, element, fields):
        for field in fields:
            if field in element:
                if not self.validate_type(element[field], fields[field]):
                    return False
            return True

    def validate(self, element, fields, required_fields, optional_fields):
        if not self.validateTypes(element, fields):
            raise ValueError("Invalid type of field")

        element_fields  = set(element.keys())
        required_fields = set(required_fields)
        optional_fields = set(optional_fields)


        if len(required_fields - element_fields) > 0:
            raise ValueError("Required field missing")

        if len(element_fields - (required_fields | optional_fields)) > 0:
            raise ValueError("Invalid field in element")