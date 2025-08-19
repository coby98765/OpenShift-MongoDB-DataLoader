from fastapi import FastAPI

from models.soldier_model import Soldier
from DAL import DAL


app = FastAPI()

@app.get("/")
def get_root():
    return {'Hello':'World'}
#CRUD
#Create
@app.post("/soldier")
async def post_soldier(data: Soldier):
    try:
        """
        TO ADD DAL CONNECTION AND QUERY
        """
        return {'Soldier Added':data}
    except Exception as e:
        print(e)
        return {"error": str(e)}

#Read
#All
@app.get("/soldiers")
async def get_soldiers():
    try:
        """
        TO ADD DAL CONNECTION AND QUERY
        """
        return {'soldiers':[]}
    except Exception as e:
        print(e)
        return {"error": str(e)}

#Singal by ID
@app.get("/soldier/{soldier_id}")
async def get_soldier(soldier_id:int):
    try:
        """
        TO ADD DAL CONNECTION AND QUERY
        """
        return {'soldier_id':soldier_id}
    except Exception as e:
        print(e)
        return {"error": str(e)}

#Update
@app.put("/soldier/{soldier_id}")
async def update_soldier(soldier_id:int,data: Soldier):
    try:
        """
        TO ADD DAL CONNECTION AND QUERY
        """
        return {'Soldier':soldier_id,
                'Updated':data}
    except Exception as e:
        print(e)
        return {"error": str(e)}

#Delete
@app.delete("/soldier/{soldier_id}")
async def delete_soldier(soldier_id:int):
    try:
        """
        TO ADD DAL CONNECTION AND QUERY
        """
        return {'Soldier Deleted':soldier_id}
    except Exception as e:
        print(e)
        return {"error": str(e)}
