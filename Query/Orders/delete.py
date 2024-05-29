from loguru import logger

from Db import execute
from load.loaderd import app
from Data.config import PATH_API


@logger.catch
@app.post(f"{PATH_API}/delete/orderId/")
async def deleteOrderId(orderId: int):
    sql = f"""DELETE FROM Orders WHERE id = %s"""
    val = (orderId, )
    return execute.delete(sql, val)