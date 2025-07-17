import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7929128384:AAFr0Obdr5EbQTFw7ZdXb7chVl1Vo46CrB4")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24219567"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d2b068e63ff5c51ff397dd500d0d51b6")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6442268649"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "beastxsrcb")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
