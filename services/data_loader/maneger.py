import DAL
from models.soldier_model import Soldier

class Maneger(object):
    def __init__(self):
        self.Dal =DAL.DAL()


    def insert_data(self,first_name,last_name,phone_number,rank):
        try:
            if not(type(first_name)==str):
                raise TypeError('First name must be a string')

            if not(type(last_name)==str):
                raise TypeError('Last name must be a string')

            if not(type(phone_number)==str and len(phone_number)!=10):
                raise TypeError('Phone number must be a number')

            if not(type(rank)==str):
                raise TypeError('Rank must be a string')

            soldier = Soldier(first_name,last_name,phone_number,rank)
            quire1 = soldier.get_quire()
            respond = self.Dal.insert_data(quire1)
            return respond

        except Exception as e:
            raise e




    def updat_data(self, soldier_id, first_name, last_name, phone_number, rank):
        try:
            if not(type(first_name)==str):
                raise TypeError('First name must be a string')

            if not(type(last_name)==str):
                raise TypeError('Last name must be a string')

            if not(type(phone_number)==str and len(phone_number)!=10):
                raise TypeError('Phone number must be a number')

            if not(type(rank)==str):
                raise TypeError('Rank must be a string')

            soldier = Soldier(first_name, last_name, phone_number, rank,soldier_id)
            quire1 = soldier.get_quire()
            respond = self.Dal.update_data(quire1)
            return respond

        except Exception as e:
            raise e


    def delete_data_by_id(self, soldier_id):
        try:
            respond = self.Dal.delete_data(soldier_id)
            return respond
        except Exception as e:
            raise e

    def get_data_by_id(self, soldier_id):
        try:
            respond = self.Dal.get_data_by_id(soldier_id)
            return respond
        except Exception as e:
            raise e


    def get_all_data(self):
        try:
            respond = self.Dal.get_all_data()
            return respond

        except Exception as e:
            raise e
