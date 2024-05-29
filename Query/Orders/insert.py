from fastapi import status

from loguru import logger

from Db import execute
from load.loaderd import app
from Data.config import PATH_API
from Entity import EntityOrders
from fastapi.responses import JSONResponse


@logger.catch
@app.post(f"{PATH_API}/insert/order/")
async def insertOrders(entityOrder: EntityOrders.EntityOrder):
    sql = "INSERT INTO Orders (nameWork, timeStart, timeEnd, description, salary, city, userAuthor, timePublish, category, subcategory, dateStart) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    val = (entityOrder.nameWork, 
           entityOrder.timeStart, 
           entityOrder.timeEnd, 
           entityOrder.description, 
           entityOrder.salary, 
           entityOrder.city, 
           entityOrder.userAuthor, 
           entityOrder.timePublish, 
           entityOrder.category, 
           entityOrder.subcategory, 
           entityOrder.dateStart)
    return execute.insert(sql, val)