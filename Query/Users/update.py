from loguru import logger

from Db import execute
from load.loaderd import app
from Data.config import PATH_API
from Entity import EntityUser

@logger.catch
@app.patch(f"{PATH_API}/update/user/nickname/")
async def updateDescription(entityUser: EntityUser.UpdateNicknameUser):
    sql = "UPDATE Users SET nickname = %s WHERE id = %s"
    val = (entityUser.nickname, entityUser.id)
    return execute.insert(sql, val)

@logger.catch
@app.patch(f"{PATH_API}/update/user/password/")
async def updateDescription(entityUser: EntityUser.UpdatePasswordUser):
    sql = "UPDATE Users SET password = %s WHERE id = %s"
    val = (entityUser.password, entityUser.id)
    return execute.insert(sql, val)