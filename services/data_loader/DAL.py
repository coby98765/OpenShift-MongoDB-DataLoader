from bson import ObjectId
from pymongo import MongoClient
from models.soldier_model import Soldier

class DAL:

    def __init__(self):
        self.client = None


    def connect(self):
        self.client = MongoClient("mongodb://localhost:27017")


    def close_conn(self):
        self.client.close()


    def get_all_data(self):
        try:
            self.connect()
            db = self.client["enemy_soldiers"]
            collection = db["soldier_details"]
            result = list(collection.find({}))
            return {"result": result}
        except Exception as e:
            print(e)
            raise {"Error": e}
        finally:
            self.close_conn()


    def get_data_by_id(self,soldier_id):
        try:
            self.connect()
            db = self.client["enemy_soldiers"]
            collection = db["soldier_details"]
            result = list(collection.find({'_id':ObjectId(soldier_id)}))
            return {'result':result}
        except Exception as e:
            print(e)
            raise {"Error": e}
        finally:
            self.close_conn()


    def insert_data(self, soldier : Soldier):
        try:
            self.connect()
            db = self.client["enemy_soldiers"]
            collection = db["soldier_details"]
            insert_data = soldier.get_query()
            inserted_id = collection.insert_one(insert_data["query"]).inserted_id
            return {"added":inserted_id}
        except Exception as e:
            print(e)
            raise {"Error": e}
        finally:
            self.close_conn()


    def update_data(self, soldier : Soldier):
        try:
            self.connect()
            db = self.client["enemy_soldiers"]
            collection = db["soldier_details"]
            update_data = soldier.get_query()
            posted = collection.update_one({'_id': ObjectId(update_data['id'])}, { '$set': update_data['query']} )
            return {"updated":posted}
        except Exception as e:
            print(e)
            raise {"Error": e}
        finally:
            self.close_conn()


    def delete_data_by_id(self, soldier_id):
        try:
            self.connect()
            db = self.client["enemy_soldiers"]
            collection = db["soldier_details"]
            result = collection.delete_one( {'_id' : ObjectId(soldier_id)}).deleted_count
            return {"deleted":result}
        except Exception as e:
            print(e)
            raise {"Error": e}
        finally:
            self.close_conn()