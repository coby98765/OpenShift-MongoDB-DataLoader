from pymongo import MongoClient
import datetime


class DAL:

    def __init__(self):
        self.client = None

    def connect(self):
        self.client = MongoClient("mongodb://localhost:27017")

    def close_conn(self):
        self.client.close()

    def get_all_data(self):
        self.connect()
        db = self.client["enemy_soldiers"]
        collection = db["soldier_details"]
        result = list(collection.find({}))
        self.close_conn()
        return str(result)

    def get_data_by_id(self,id):
        self.connect()
        db = self.client["enemy_soldiers"]
        collection = db["soldier_details"]
        result = list(collection.find({'id':id}))
        self.close_conn()
        return str(result)

    def insert_data(self):
        self.connect()
        post = self.get_data()
        db = self.client["enemy_soldiers"]
        posts = db["soldier_details"]
        post_id = posts.insert_one(post)
        self.close_conn()
        return 'the data is inserted!'


    def update_data(self, id, first_name, last_name, phone_number, rank):
        self.connect()
        db = self.client["enemy_soldiers"]
        posts = db["soldier_details"]
        post_id = posts.updateOne({'_id': id}, { '$set': {'first_name': first_name, 'kast_name':last_name, 'phone_number':phone_number, 'rank':rank}} )
        self.close_conn()
        return "the database is updated!"

    def delete_data_by_id(self,id):
        self.connect()
        db = self.client["enemy_soldiers"]
        db.soldier_details.deleteOne({'_id':id})
        self.close_conn()
        return 'the data is deleted!'

    def get_data(self):
        return {
            "_id":203,
            "first_name": "yossi",
            "last_name": "SHBB adb  ad!",
            "phone_number": '0585204770',
            "rank": "iushsz",
        }




a = DAL()
a.delete_data_by_id(203)
print(a.get_all_data())

