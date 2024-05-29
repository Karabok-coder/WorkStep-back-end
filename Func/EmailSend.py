from Func.Utils import Rand, EmailSender
from load.loaderd import app
from Data.config import PATH_API
from Entity import EntityEmail

@app.post(f"{PATH_API}/EmailCode")
async def read_item(entity: EntityEmail.Email):
    code = Rand.Rand(entity.seed).toUntilInt(100000, 999999)
    EmailSender.Sender().sendCode(code, entity.username, entity.email)
    return True