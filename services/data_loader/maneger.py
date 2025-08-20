import DAL
from models.soldier_model import Soldier

class Maneger:
    def __init__(self):
        self.Dal =DAL.DAL()


    def insert_data(self,data:dict):
        try:
            if not(type(data['first_name'])==str):
                raise TypeError('First name must be a string')

            if not(type(data['last_name'])==str):
                raise TypeError('Last name must be a string')

            if not(type(data['phone_number'])==str and len(data['phone_number'])!=10):
                raise TypeError('Phone number must be a number')

            if not(type(data['rank'])==str):
                raise TypeError('Rank must be a string')

            soldier = Soldier(data['first_name'],data['last_name'],data['phone_number'],data['rank'])
            quire1 = soldier.get_quire()
            respond = self.Dal.insert_data(quire1)
            return respond

        except Exception as e:
            raise Exception(e)




    def updat_data(self,soldier_id, data:dict):
        try:
            if not (type(data['first_name']) == str):
                raise TypeError('First name must be a string')

            if not (type(data['last_name']) == str):
                raise TypeError('Last name must be a string')

            if not (type(data['phone_number']) == str and len(data['phone_number']) != 10):
                raise TypeError('Phone number must be a number')

            if not (type(data['rank']) == str):
                raise TypeError('Rank must be a string')

            soldier = Soldier(data['first_name'],data['last_name'],data['phone_number'],data['rank'],soldier_id)
            quire1 = soldier.get_quire()
            respond = self.Dal.update_data(quire1)
            return respond

        except Exception as e:
            raise Exception(e)


    def delete_data_by_id(self, soldier_id):
        try:
            respond = self.Dal.delete_data_by_id(soldier_id)
            return respond
        except Exception as e:
            raise Exception({"Error": str(e)})

    def get_data_by_id(self, soldier_id):
        try:
            respond = self.Dal.get_data_by_id(soldier_id)
            if not respond:
                raise
            return respond
        except Exception as e:
            raise Exception(e)


    def get_all_data(self):
        try:
            respond = self.Dal.get_all_data()
            return respond

        except Exception as e:
            raise Exception(e)
