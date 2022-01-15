import json
import os


def get_user_list(config, key):
    with open('{}/MashaRoBot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER = True
  
    TEMP_DOWNLOAD_DIRECTORY = 'None'
    API_ID = 7679848
    API_HASH = "bf6275a102d4a661f7c2cc5883e893a2"
    TOKEN = "5069939361:AAHO_n2qIkefFiH6eiPvETndL98-20cYcz8"
    OWNER_ID = 5003025270  
    OWNER_USERNAME = "DreamerNo1"
    SUPPORT_CHAT = 'NovusSupport'
    JOIN_LOGGER = -1001688865879
    EVENT_LOGS = -1001688865879

    ALLOW_CHATS = "True"
    SQLALCHEMY_DATABASE_URI = 'postgres://numeldxg:16D1zjUkYUtZUO10s7_IN-01UcfWAT8w@john.db.elephantsql.com/numeldxg'  
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = None
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "UEYs6snrsr2aDrrgtiRAs_rIqCKBxCGj2QBtpYYGs5Elu3Gc_mQG_FjxPF9IUaJS"  
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    BOT_ID = "5069939361"
    
    DRAGONS = get_user_list('elevated_users.json', 'sudos')

    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = ''  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = 'awoo'  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = 'awoo'  # Get your API key from https://timezonedb.com/api
    WALL_API = 'awoo'  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = 'awoo'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
