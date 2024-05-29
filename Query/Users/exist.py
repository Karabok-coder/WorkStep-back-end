from loguru import logger

from Db import execute
from load.loaderd import app
from Data.config import PATH_API
from Entity import EntityUser


@logger.catch
@app.post(f"{PATH_API}/exist/userEmail/")
async def existUserEmail(entity: EntityUser.ExistUserEmail):
    sql = f"SELECT COUNT(*) FROM Users WHERE email = '{entity.email}';"
    return execute.selectExecute(sql)[0][0]


@logger.catch
@app.post(f"{PATH_API}/exist/userNickname/")
async def existUserNickname(entity: EntityUser.ExistUserNickname):
    sql = f"SELECT COUNT(*) FROM Users WHERE nickname = '{entity.nickname}';"
    return execute.selectExecute(sql)[0][0]