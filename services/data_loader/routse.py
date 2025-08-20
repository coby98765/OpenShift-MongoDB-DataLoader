from fastapi import FastAPI, HTTPException

from maneger import Maneger
from utils import  Utils

manager = Maneger()
app = FastAPI()

@app.get("/")
def get_root():
    return {'Hello':'World'}
#CRUD
#Create
@app.post("/soldier")
async def post_soldier(data: dict):
    try:
        res = manager.insert_data(data)
        return {'Soldier Added':res}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail={"error": str(e)})

#Read
#All
@app.get("/soldiers")
async def get_soldiers():
    try:
        res = manager.get_all_data()
        res = Utils.correct_the_id(res)
        return {'soldiers':res}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail={"error": str(e)})

#Singal by ID
@app.get("/soldier/{soldier_id}")
async def get_soldier(soldier_id:str):
    try:
        res = manager.get_data_by_id(soldier_id)
        res = Utils.correct_the_id(res)
        return {'soldier':res}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail={"error": str(e)})

#Update
@app.put("/soldier/{soldier_id}")
async def update_soldier(soldier_id:str,data: dict):
    try:
        res = manager.updat_data(soldier_id,data)
        return {'Soldier':soldier_id,
                'Updated':res}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail={"error": str(e)})

#Delete
@app.delete("/soldier/{soldier_id}")
async def delete_soldier(soldier_id:str):
    try:
        res = manager.delete_data_by_id(soldier_id)
        return {'Soldier Deleted':res}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail={"error": str(e)})
