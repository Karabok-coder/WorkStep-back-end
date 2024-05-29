from fastapi.responses import JSONResponse
from fastapi import status

from mysql.connector import Error

from loguru import logger

from Db import connect
from datetime import timedelta
from datetime import datetime
from datetime import date


@logger.catch
def _exec(sql: str, values):
    try:
        connection = connect.con()    
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()
        inserted_id = cursor.lastrowid
        return JSONResponse(content={"err": False, "val": inserted_id}, status_code=status.HTTP_200_OK)
    except Error as e:
        return JSONResponse(content={"err": e.msg}, status_code=status.HTTP_400_BAD_REQUEST)
    finally:
        cursor.close()
        connection.close()

@logger.catch
def select(sql: str) -> str | None:
    try:
        connection = connect.con()    
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        data = {}
        for row in result:
            row_dict = {}
            for i, value in enumerate(row):
                # Преобразование timedelta в количество секунд
                if isinstance(value, timedelta):
                    row_dict[cursor.column_names[i]] = int(value.total_seconds())
                elif isinstance(value, datetime):
                    row_dict[cursor.column_names[i]] = f"{value.date()}T{value.time()}"
                elif isinstance(value, date):
                    row_dict[cursor.column_names[i]] = f"{value.year}-{value.month}-{value.day}"
                else:
                    row_dict[cursor.column_names[i]] = value
            data[row[0]] = row_dict
        return JSONResponse(content={"content": data}, status_code=status.HTTP_200_OK)
    except Error as e:
        return JSONResponse(content={"err": e.msg}, status_code=status.HTTP_400_BAD_REQUEST)
    finally:
        cursor.close()
        connection.close()

@logger.catch
def selectExecute(sql: str) -> str | None:
    try:
        connection = connect.con()    
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        
        return result
    except Error as e:
        return e.msg
    finally:
        cursor.close()
        connection.close()

@logger.catch
def insert(sql: str, values):
    return _exec(sql, values)

@logger.catch
def update(sql: str, values):
    return _exec(sql, values)

@logger.catch
def delete(sql: str, values):
    return _exec(sql, values)