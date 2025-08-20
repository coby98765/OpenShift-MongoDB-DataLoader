from bson import ObjectId
from pymongo import MongoClient ,errors
import os


class DAL:

    def __init__(self):
        self.client = None
        self.host = os.getenv("DB_HOST","localhost")
        self.db_name = os.getenv("DB_NAME","enemy_soldiers")
        self.db_coll = os.getenv("DB_COLL","soldier_details")
        self.db_port = os.getenv("BD_PORT","27017")


    def connect(self):
        try:
            self.client = MongoClient(f"mongodb://{self.host}:{self.db_port}")
            self.client.admin.command("ping")
            print(f"Connected to {self.host}!")
        except errors.ServerSelectionTimeoutError as err:
            print(f"Server selection timeout: {err}")
            raise
        except errors.ConnectionFailure as err:
            print(f"Connection failed: {err}")
            raise
        except errors.ConfigurationError as err:
            print(f"Configuration error: {err}")
            raise
        except Exception as err:
            print(f"Unexpected error: {err}")
            raise

    def close_conn(self):
        self.client.close()


    def get_all_data(self):
        try:
            self.connect()
            db = self.client[self.db_name]
            collection = db[self.db_coll]
            result = list(collection.find({}))
            return {"result": result}
        except Exception as e:
            print(e)
            raise Exception(e)
        finally:
            self.close_conn()


    def get_data_by_id(self,soldier_id):
        try:
            self.connect()
            db = self.client[self.db_name]
            collection = db[self.db_coll]
            result = list(collection.find({'_id':ObjectId(soldier_id)}))
            return result
        except Exception as e:
            print(e)
            raise Exception(e)
        finally:
            self.close_conn()


    def insert_data(self, insert_data : dict):
        try:
            self.connect()
            db = self.client[self.db_name]
            collection = db[self.db_coll]
            inserted_id = collection.insert_one(insert_data["query"]).inserted_id
            return {"added":inserted_id}
        except Exception as e:
            print(e)
            raise Exception(e)
        finally:
            self.close_conn()


    def update_data(self, update_data : dict):
        try:
            self.connect()
            db = self.client[self.db_name]
            collection = db[self.db_coll]
            posted = collection.update_one({'_id': ObjectId(update_data['id'])}, { '$set': update_data['query']} )
            return {"updated":posted}
        except Exception as e:
            print(e)
            raise Exception(e)
        finally:
            self.close_conn()


    def delete_data_by_id(self, soldier_id):
        try:
            self.connect()
            db = self.client[self.db_name]
            collection = db[self.db_coll]
            result = collection.delete_one( {'_id' : ObjectId(soldier_id)}).deleted_count
            return {"deleted":result}
        except Exception as e:
            print(e)
            raise Exception(e)
        finally:
            self.close_conn()
