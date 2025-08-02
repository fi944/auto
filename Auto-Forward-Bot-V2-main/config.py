from os import environ 

class Config:
    API_ID = environ.get("API_ID", "10122221")
    API_HASH = environ.get("API_HASH", "0599f028e8b0e5ac86dc36cbe32d87d8")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7594886219:AAE0-iPwo1y38QTeRMkocxcGCt-v_9B2ksM") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '881535564').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
