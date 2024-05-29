from fastapi import FastAPI

from loguru import logger

from Data.config import PATH_LOGS

app = FastAPI()

logger.add(PATH_LOGS,
           format='{time}, {level}, {file}, {line}, {message}', 
           level="DEBUG", 
           rotation="10 MB", 
           compression="zip")
