from fastapi import status

from loguru import logger

from Db import execute
from load.loaderd import app
from Data.config import PATH_API
from Entity import EntityProfile


@logger.catch
@app.post(f"{PATH_API}/insert/profile/")
async def insertProfile(entity: EntityProfile.ProfileInsert):
    sql = "INSERT INTO Profiles (firstName, userId) values (%s, %s);"
    val = (entity.firstName, entity.userId)
    return execute.insert(sql, val)
