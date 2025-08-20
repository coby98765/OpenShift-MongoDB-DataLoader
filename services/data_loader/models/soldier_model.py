class Soldier:
    def __init__(self,first_name,last_name,phone_number,rank,soldier_id=None):
        self.id=soldier_id
        self.first_name=first_name
        self.last_name=last_name
        self.phone_number=phone_number
        self.rank=rank


    def get_quire(self):
        return {'id':self.id,
            'query':{'first_name':self.first_name,'last_name':self.last_name,'phone_number':self.phone_number,'rank':self.rank}}

