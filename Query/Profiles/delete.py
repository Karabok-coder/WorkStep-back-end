from loguru import logger

from Db import execute
from load.loaderd import app
from Data.config import PATH_API
from Entity import EntityProfile


@logger.catch
@app.delete(f"{PATH_API}/delete/profileId")
async def deleteProfileId(entity: EntityProfile.ProfileDelete):
    sql = "DELETE FROM Profiles WHERE id = %s"
    val = (entity.id, )
    return execute.delete(sql, val)
