from mysql.connector import connect, Error

from loguru import logger

from Data.config import HOST, PORT, USER, PASSWORD, DATABASE


@logger.catch
def con():
    try:
        return connect( host=HOST,
                        port=PORT,
                        user=USER,
                        password=PASSWORD,
                        database=DATABASE)
    except Error as e:
        logger.error(e)