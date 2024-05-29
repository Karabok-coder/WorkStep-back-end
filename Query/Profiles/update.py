from loguru import logger

from Db import execute
from load.loaderd import app
from Data.config import PATH_API


@logger.catch
@app.patch(f"{PATH_API}/update/profile/description/")
async def updateDescription(description: str, id: int):
    sql = "UPDATE Profiles SET description = %s WHERE id = %s"
    val = (description, id)
    return execute.insert(sql, val)