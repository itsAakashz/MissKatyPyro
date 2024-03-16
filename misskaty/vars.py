
import sys
from logging import getLogger
from os import environ

import dotenv

LOGGER = getLogger("MissKaty")

dotenv.load_dotenv("config.env", override=True)

if API_ID := environ.get("API_ID", "11457698"):
    API_ID = int(API_ID)
else:
    LOGGER.error("API_ID variable is missing! Exiting now")
    sys.exit(1)
API_HASH = environ.get("API_HASH", "4000b13f-01ff-4be8-beba-26ef349bfaab")
if not API_HASH:
    LOGGER.error("API_HASH variable is missing! Exiting now")
    sys.exit(1)
BOT_TOKEN = environ.get("BOT_TOKEN", "1814993176:AAE_2SG0FT1fpt9xCamywkckh6ttDHgBggg")
if not BOT_TOKEN:
    LOGGER.error("BOT_TOKEN variable is missing! Exiting now")
    sys.exit(1)
DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://Aakash:zatrop@cluster0.h71fvqs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
if not DATABASE_URI:
    LOGGER.error("DATABASE_URI variable is missing! Exiting now")
    sys.exit(1)
if LOG_CHANNEL := environ.get("LOG_CHANNEL", "1097379245"):
    LOG_CHANNEL = int(LOG_CHANNEL)

else:
    LOGGER.error("LOG_CHANNEL variable is missing! Exiting now")
    sys.exit(1)
# Optional ENV
LOG_GROUP_ID = environ.get("LOG_GROUP_ID")
USER_SESSION = environ.get("USER_SESSION")
DATABASE_NAME = environ.get("DATABASE_NAME", "MissKatyDB")
TZ = environ.get("TZ", "Asia/Jakarta")
COMMAND_HANDLER = environ.get("COMMAND_HANDLER", "! /").split()
SUDO = list(
    {
        int(x)
        for x in environ.get(
            "SUDO",
            "617426792 2024984460",
        ).split()
    }
)
SUPPORT_CHAT = environ.get("SUPPORT_CHAT", "#")
AUTO_RESTART = environ.get("AUTO_RESTART", False)
OPENAI_KEY = environ.get("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")
GOOGLEAI_KEY = environ.get("AIzaSyBsJlGcK07lLL6q13LbDPIbXwp3-CrZTgg")

## Config For AUtoForwarder
# Forward From Chat ID
FORWARD_FROM_CHAT_ID = list(
    {
        int(x)
        for x in environ.get(
            "FORWARD_FROM_CHAT_ID",
            "-1097379245 -1097379245 -1097379245",
        ).split()
    }
)
# Forward To Chat ID
FORWARD_TO_CHAT_ID = list(
    {int(x) for x in environ.get("FORWARD_TO_CHAT_ID", "-1097379245").split()}
)
FORWARD_FILTERS = list(set(environ.get("FORWARD_FILTERS", "video document").split()))
BLOCK_FILES_WITHOUT_EXTENSIONS = bool(
    environ.get("BLOCK_FILES_WITHOUT_EXTENSIONS", True)
)
BLOCKED_EXTENSIONS = list(
    set(
        environ.get(
            "BLOCKED_EXTENSIONS",
            "html htm json txt php gif png ink torrent url nfo xml xhtml jpg",
        ).split()
    )
)
MINIMUM_FILE_SIZE = environ.get("MINIMUM_FILE_SIZE")
CURRENCY_API = environ.get("8DIIPVROWD8S2CLJ")
