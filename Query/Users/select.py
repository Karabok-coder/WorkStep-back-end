from loguru import logger

from Db import execute
from load.loaderd import app
from Data.config import PATH_API


@logger.catch
@app.get(f"{PATH_API}/select/allUsers/")
async def allUsers():
    sql = f"SELECT * FROM Users"
    return execute.select(sql)
        
@logger.catch
@app.post(f"{PATH_API}/select/nicknameUser/")
async def nicknameUser(nickname: str):
    sql = f"SELECT * FROM Users where nickname = '{nickname}';"
    return execute.select(sql)

@logger.catch
@app.post(f"{PATH_API}/select/idUser/")
async def idUser(id: int):
    sql = f"SELECT * FROM Users where id = {id}"
    return execute.select(sql)

@logger.catch
@app.post(f"{PATH_API}/select/emailUser/")
async def emailUser(email: str):
    sql = f"SELECT * FROM Users where email = '{email}'"
    return execute.select(sql)
