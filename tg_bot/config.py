from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 830359032  # my telegram ID
    OWNER_USERNAME = "DaRrKNneSs_1"  # my telegram username
    API_KEY = "6202877672:AAEGcsfAESRZGXYuX2g2SJwm5pRw62zZQws"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://oufnqgyb:QKtc9JZLGagCRjunNu_RZ-Gj1-dlxt_9@queenie.db.elephantsql.com/oufnqgyb'  # sample db credentials
    MESSAGE_DUMP = '-1001889729935' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [830359032]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
