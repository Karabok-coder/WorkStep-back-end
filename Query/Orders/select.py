from loguru import logger

from Db import execute
from load.loaderd import app
from Data.config import PATH_API
from Entity import EntityOrders

@logger.catch
@app.get(f"{PATH_API}/select/order/")
async def allOrders():
    sql = """
        SELECT * FROM Orders"""
    return execute.select(sql)

@logger.catch
@app.post(f"{PATH_API}/select/orderUserId/")
async def allOrders(userId: int):
    sql = f"""SELECT * FROM Orders where userAuthor = {userId}"""
    return execute.select(sql)

@logger.catch
@app.post(f"{PATH_API}/select/ordersFilter/")
async def allOrders(entityOrders: EntityOrders.EntitySelectFilter):

    print("asdasd")

    if not bool(entityOrders.salaryStart):
        entityOrders.salaryStart = "null"
    else:
        entityOrders.salaryStart = f'"{entityOrders.salaryStart}"'

    if not bool(entityOrders.salaryEnd):
        entityOrders.salaryEnd = "null"
    else:
        entityOrders.salaryEnd = f'"{entityOrders.salaryEnd}"'

    if not bool(entityOrders.category):
        entityOrders.category = "null"
    else:
        entityOrders.category = f'"{entityOrders.category}"'

    if not bool(entityOrders.subcategory):
        entityOrders.subcategory = "null"
    else:
        entityOrders.subcategory = f'"{entityOrders.subcategory}"'

    if not bool(entityOrders.city):
        entityOrders.city = "null"
    else:
        entityOrders.city = f'"{entityOrders.city}"'

    if not bool(entityOrders.dateStart):
        entityOrders.dateStart = "null"
    else:
        entityOrders.dateStart = f'"{entityOrders.dateStart}"'
        # entityOrders.dateStart = entityOrders.dateStart.replace('.', '-')

    if not bool(entityOrders.dateEnd):
        entityOrders.dateEnd = "null"
    else:
        entityOrders.dateEnd = f'"{entityOrders.dateEnd}"'
        # entityOrders.dateEnd = entityOrders.dateEnd.replace('.', '-')


    sql = f"""SELECT *
              FROM Orders
              WHERE
                  ({entityOrders.salaryStart} IS NULL OR salary > {entityOrders.salaryStart}) AND
                  ({entityOrders.salaryEnd} IS NULL OR {entityOrders.salaryEnd} > salary) AND
                  ({entityOrders.category} IS NULL OR category = {entityOrders.category}) AND
                  ({entityOrders.subcategory} IS NULL OR subcategory = {entityOrders.subcategory}) AND
                  ({entityOrders.city} IS NULL OR city = {entityOrders.city}) AND
                  ({entityOrders.dateStart} IS NULL OR dateStart > {entityOrders.dateStart}) AND
                  ({entityOrders.dateEnd} IS NULL OR {entityOrders.dateEnd} > dateStart);"""

    return execute.select(sql)