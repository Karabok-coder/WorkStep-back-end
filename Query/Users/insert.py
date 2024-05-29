from loguru import logger

from Db import execute
from load.loaderd import app
from Data.config import PATH_API
from Entity.EntityUser import EntityUser


@logger.catch
@app.post(f"{PATH_API}/insert/user/")
async def insertUser(entityUser: EntityUser):
    sql = "INSERT INTO Users (email, password, nickname, dateReg) VALUES (%s, %s, %s, %s);"
    values = (entityUser.email,
              entityUser.password,
              entityUser.nickname, 
              entityUser.dateReg)
    return execute.insert(sql, values)
