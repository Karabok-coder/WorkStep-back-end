from Query import *
from Func import *
from Chat import *

import uvicorn

from load.loaderd import app

from loguru import logger
from Data import config

@logger.catch
@app.get("/politic", response_class=HTMLResponse)
async def politic():
    with open(config.PATH_POLITIC, 'r') as file:
        return file.read()


uvicorn.run(app=app)