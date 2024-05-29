from loguru import logger

from Db import execute
from load.loaderd import app
from Data.config import PATH_API

@logger.catch
@app.post(f"{PATH_API}/select/userIdProfile/")
async def userIdProfile(userId: int):
    sql = f"SELECT * FROM Profiles where userId = {userId}"
    return execute.select(sql)

@logger.catch
@app.post(f"{PATH_API}/select/idProfile")
async def idProfile(id: int):
    sql = f"SELECT * FROM Profiles where id = {id}"
    return execute.select(sql)

@logger.catch
@app.get(f"{PATH_API}/select/allProfile/")
async def allProfile():
    sql = f"SELECT * FROM Profiles"
    return execute.select(sql)