import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7578652576:AAHnx7gkH3LTZ-tEI8gyQO5SaRt4Ljkz_zM")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21175909"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "7416d74b021bea39a71446003843d11c")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1008926477"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "beastxsrcb")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
